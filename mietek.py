#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------
#     ~MIETEK~ 
#    the chatbot
# -----------------
#  (c)2017 KJ/P1X

import filesystem
import config
import os, slackclient, time, re, random
from asciimatics.scene import Scene
from asciimatics.screen import Screen

VERSION = 0.6
SOCKET_DELAY = 1
BOT_SLACK_NAME = 'mietek'
BOT_SLACK_TOKEN = os.environ.get('SLACK_MIETEK_TOKEN')
BOT_SLACK_ID = os.environ.get('BOT_MIETEK_ID')
BOARD_MSG_LEN_MIN = 3
BOARD_MSG_LEN_MAX = 0
sc = slackclient.SlackClient(BOT_SLACK_TOKEN)
fs = filesystem.Filesystem()
cfg = config.Config()
def get_mention(user):
    return '<@{user}>'.format(user=user)
bot_slack_mention = get_mention(BOT_SLACK_ID)
logger = []
board = fs.load()

CMD_BOARD = ['tablica', 'Zapisalem na tablicy :)', 'Wiadomosc musi byc dluzsza niz {min} znaki i krotsza niz {max} znakow.']
CMD_REMIND = ['przypomnij', 'Postaram sie przypomniec']
CMDS = [
    [
        ['witam', 'witaj', 'czesc', 'hi', 'yo', 'elo', 'siema'],
        ['Witam pana kierownika!', 'Uszanowanie!', 'Witaj, {mention}']
    ],
    [
        ['wino', 'winiacz', 'piwo', 'piwko', 'browar'],
        ['Alkohol?', 'Napil bym sie...']
    ],
    [
        ['chuj', 'chuju', 'burak', 'debil'],
        ['A po co zaraz tak wulgarnie?', 'Taki mocny w gebie to moze poratujesz 50gr?']
    ],
    [
        ['pearson', 'ioki', 'korpo'],
        ['Szlachta nie pracuje!', 'Korposzczury...']
    ]
]

def save_whiteboard(message):
    message = message.replace(CMD_BOARD[0], '').strip()
    ml = len(message)
    if ml > BOARD_MSG_LEN_MIN and ml < BOARD_MSG_LEN_MAX:
        board.append('[!] ' + message)
        fs.save(board)
        return CMD_BOARD[1]
    else:
        return CMD_BOARD[2].format(min=BOARD_MSG_LEN_MIN, max=BOARD_MSG_LEN_MAX)

def decode_message(message):
    if message:
        tokens = [re.sub('[^A-Za-z0-9]+', '', word.lower()) for word in message.strip().split()]
        
        # real commands
        if tokens[0] == CMD_BOARD[0]:
            return save_whiteboard(message)
    
        # smalltalk
        for cmd in CMDS:
            if any(g in tokens for g in cmd[0]):
                return random.choice(cmd[1]) 
    return False

def format_response(response, user_mention):
    return response.format(mention=user_mention)

def handle_message(message, user, channel):
    message_decoded = decode_message(message)
    if message_decoded:
        user_mention = get_mention(user)
        post_message(message=format_response(message_decoded, user_mention), channel=channel)

def is_for_me(event):
    type = event.get('type')
    if type and type == 'message' and not(event.get('user') == BOT_SLACK_ID):
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
    sc.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)

def format_log(event):
    log = '[+] ' + str(event.get('type'))
    if event.get('user'):
        log += ' <' + str(event.get('user')) + '> '
    if event.get('text'):
        log += str(event.get('text'))
    return log


def draw_data(scr, data, title, x, y, show_last, color):
    top_y = y
    max_x = scr.width
    for i in range(len(data)-show_last, len(data)):
        if i > -1 and i < len(data):
            scr.move(x,y)
            scr.draw(max_x-2, y, ' ', scr.COLOUR_WHITE, color)
            scr.print_at(data[i] + ' ',x, y, scr.COLOUR_BLACK, 0, color)
        y += 1
    render_frame(scr, title, 0, top_y, max_x-1, y+1, color)
def render_frame(scr, title, x, y, max_x, max_y, color,):
    scr.move(x,y)
    scr.draw(max_x, y, None, color, thin=True)
    scr.draw(max_x, max_y, None, color, thin=True)
    scr.draw(x, max_y, None, color, thin=True)
    scr.draw(x, y, None, color, thin=True)
    scr.print_at(title, int(max_x/2)-int(len(title)/2), y, color, scr.A_BOLD)

def draw_footer(scr):
    scr.print_at('[?] Napisz cos! wyslij wiadomosc *tablica tresc* do @mietek na firmowym Slacku!.', 1, scr.height-3, scr.COLOUR_YELLOW)
    scr.print_at('[?] Nacisnij [Q] aby wylaczyc bota.', 1, scr.height-2, scr.COLOUR_RED)

def draw_header(scr):
    scr.move(0, 0)
    scr.draw(scr.width, 0, None, scr.COLOUR_GREEN)
    title = ' ~ MIETEK the chatbot - v' + str(VERSION) + ' ~ '
    scr.print_at(title, int(scr.width/2)-int(len(title)/2), 0, scr.COLOUR_GREEN, scr.A_BOLD)    

def loop(scr):
    global logger
    global board
    global BOARD_MSG_LEN_MAX
    draw_header(scr)
    draw_footer(scr)
    logger.append('[.] Mietek is alive!')
    BOARD_MSG_LEN_MAX = scr.width - 4

    while True:
        event_list = sc.rtm_read()
        if len(event_list) > 0:
            for event in event_list:
                logger.append(format_log(event))
                if is_for_me(event):
                    handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))

        ev = scr.get_key()
        if ev in (ord('Q'), ord('q')):
            raise StopApplication("User requested exit")
        
        draw_data(scr, logger, ' ~ LOG WINDOW ~ ', 2, 2, 6, scr.COLOUR_RED)
        draw_data(scr, board, ' ~ WHITEBOARD ~ ', 2, 10, scr.height - 18, scr.COLOUR_WHITE)
        scr.refresh()            
        time.sleep(SOCKET_DELAY)

if __name__=='__main__':
    print('[.] ~MIETEK~ the chatbot v' + str(VERSION))
    print('[.] Connecting...')
    if sc.rtm_connect():
        Screen.wrapper(loop)
    else:
        print('[!] Connection to Slack failed.')


