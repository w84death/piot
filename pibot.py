#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PiBot - Intranet Chatbot System 
#
# see LICENSE file for licence
# see README.md for more info
# see CHANGELOG.md for detailed changes in each version
#
# (c) 2017 kj/P1X
#

# external libs
import os, slackclient, time, re, random
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# internal libs
import filesystem
import config
import logger
import commands
import whiteboard
import forecast
import psas

fs = filesystem.Filesystem()
cfg = config.Config()
log = logger.Logger()
cmds = commands.Commands()
wb = whiteboard.Whiteboard()
fc = forecast.Forecast()
sc = slackclient.SlackClient(cfg.get_api_key('slack'))
psa = psas.PublicServiceAnnaucments()

def get_mention(user):
    return '<@{user}>'.format(user=user)
bot_slack_mention = get_mention(cfg.get_api_key('bot'))


# The BRAIN

def decode_message(message, user):
    if message:
        tokens = [re.sub('[^A-Za-z0-9]+', '', word.lower()) for word in message.strip().split()]
        
        # real commands
        if tokens[0] == cmds.get_cmd('board')['cmd']:
            return wb.write(message)

        if tokens[0] == cmds.get_cmd('forecast')['cmd']:
            return fc.get_report()

        # smalltalk
        for chat in cmds.get_chat():
            if any(g in tokens for g in chat[0]):
                return random.choice(chat[1]) 
    return False

def format_response(response, user_mention):
    return response.format(mention=user_mention)

def handle_message(message, user, channel):
    message_decoded = decode_message(message, user)
    if message_decoded:
        user_mention = get_mention(user)
        post_message(message=format_response(message_decoded, user_mention), channel=channel)

def is_for_me(event):
    type = event.get('type')
    if type and type == 'message' and not(event.get('user') == cfg.get_api_key('bot')):
        if is_private(event):
            return True
        text = event.get('text')
        channel = event.get('channel')
        if bot_slack_mention in text.strip().split():
            return True
    return False

def is_private(event):
    return event.get('channel').startswith('D')

def post_message(message, channel):
    sc.api_call('chat.postMessage', 
        channel = channel,
        text = message, 
        as_user = True)
    return True



def draw_data(scr, data, title, x, y, show_last, color):
    top_y = y
    max_x = scr.width
    for i in range(len(data)-show_last, len(data)):
        scr.move(x,y)
        scr.draw(max_x-1, y, ' ', scr.COLOUR_WHITE, color)    
        if i > -1 and i < len(data):
            scr.print_at(str(data[i]), x, y, scr.COLOUR_BLACK, 0, color)
        y += 1
    render_frame(scr, title, 0, top_y, max_x-1, y, color)
    return True

def render_frame(scr, title, x, y, max_x, max_y, color):
    scr.move(x,y)
    scr.draw(max_x, y, None, color)
    scr.draw(max_x, max_y, None, color)
    scr.draw(x, max_y, None, color)
    scr.draw(x, y, None, color)
    scr.print_at(' {title} '.format(title=title), cfg.get_settings('window_title_pos'), y, color, scr.A_BOLD)
    return True

def draw_footer(scr):
    scr.print_at('[?] Napisz cos! wyslij wiadomosc *tablica tresc* do @mietek na firmowym Slacku!.', 1, scr.height-3, scr.COLOUR_YELLOW)
    scr.print_at('[?] Nacisnij [Q] aby wylaczyc bota.', 1, scr.height-2, scr.COLOUR_RED)

def draw_header(scr):
    scr.move(0, 0)
    scr.draw(scr.width, 0, None, scr.COLOUR_GREEN)
    title = ' {app_name} [v{version}] '.format(
        app_name = cfg.get_settings('app_name'),
        version = cfg.get_settings('version'))
    scr.print_at(title, cfg.get_settings('window_title_pos'), 0, scr.COLOUR_GREEN, scr.A_BOLD)    


def loop(scr):
    draw_header(scr)
    draw_footer(scr)
    log.save(cmds.get_psa('welcome'))

    while True:
        event_list = sc.rtm_read()
        if len(event_list) > 0:
            for event in event_list:
                log.save_event(event)
                if is_for_me(event):
                    handle_message(
                        message = event.get('text'), 
                        user = event.get('user'), 
                        channel = event.get('channel'))

        ev = scr.get_key()
        if ev in (ord('Q'), ord('q')):
            raise StopApplication("User requested exit")
        
        wb.write(psa.check_scheduler(), True)
        draw_data(scr, log.get_log(), cfg.get_settings('window_title_log'), 1, 2, 6, scr.COLOUR_RED)
        draw_data(scr, wb.get_board(), cfg.get_settings('window_title_board'), 1, 10, scr.height - 15, scr.COLOUR_WHITE)
        scr.refresh()            
        time.sleep(cfg.get_settings('delay'))

if __name__=='__main__':
    print('[.] {app_name} [v{version}]'.format(
        app_name = cfg.get_settings('app_name'),
        version = cfg.get_settings('version')))
    print('[.] Connecting...')
    if sc.rtm_connect():
        Screen.wrapper(loop)
    else:
        print('[!] Connection to Slack failed.')
