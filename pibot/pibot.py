#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PIBOT ZERO - Intranet Chatbot System 
#
# see LICENSE file for licence
# see README.md for more info
# see CHANGELOG.md for detailed changes in each version
#
# change config.py for your needs
# run pibot.py to start bot
#
# (c) 2017 kj/P1X
#

# external libs
import os, slackclient, time, re, random

# internal libs
import filesystem, config, logger, display_fast, commands
import whiteboard, forecast, psas

fs = filesystem.Filesystem()
cfg = config.Config()
log = logger.Logger()
cmds = commands.Commands()
wb = whiteboard.Whiteboard()
fc = forecast.Forecast()
sc = slackclient.SlackClient(cfg.get_api_key('slack'))
psa = psas.PublicServiceAnnaucments()
disp = display_fast.Display()

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

def render_screen():
    disp.clear()
    disp.draw_header() 
    disp.draw_data(log.get_log(), 
        cfg.get_settings('window_title_log'), 
        cfg.get_settings('window_rows_log'),
        cfg.get_style('cyan'))
    disp.draw_data(wb.get_board(),
        cfg.get_settings('window_title_board'), 
        cfg.get_settings('window_rows_board'),
        cfg.get_style('white'))
    disp.draw_footer()
    return True

def loop():
    log.save(cmds.get_psa('welcome'))
    disp.draw_header()
    disp.draw_footer()
    
    while True:
        event_list = sc.rtm_read()
        redraw_screen = False
        
        if len(event_list) > 0:
            for event in event_list:
                log.save_event(event)
                if is_for_me(event):
                    handle_message(
                        message = event.get('text').encode('ascii', 'replace'),
                        user = event.get('user'), 
                        channel = event.get('channel'))
                redraw_screen = True
       
        wb.write(psa.check_scheduler(), True)
        
        if redraw_screen: 
            render_screen()            
    
        time.sleep(cfg.get_settings('delay'))

if __name__=='__main__':
    print('[.] {app_name} [v{version}]'.format(
        app_name = cfg.get_settings('app_name'),
        version = cfg.get_settings('version')))
    print('[.] Connecting...')
    if sc.rtm_connect():
        loop()
    else:
        print('[!] Connection to Slack failed.')
