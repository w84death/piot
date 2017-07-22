#!/bin/python
# -----------------
#     ~MIETEK~ 
#    the chatbot
# -----------------
#  (c)2017 KJ/P1X

import os, slackclient, time, re, random

SOCKET_DELAY = 1
BOT_SLACK_NAME = 'mietek'
BOT_SLACK_TOKEN = os.environ.get('SLACK_MIETEK_TOKEN')
BOT_SLACK_ID = os.environ.get('BOT_MIETEK_ID')
sc = slackclient.SlackClient(BOT_SLACK_TOKEN)
def get_mention(user):
    return '<@{user}>'.format(user=user)
bot_slack_mention = get_mention(BOT_SLACK_ID)

CMDS = [
    [
        ['witam', 'czesc', 'hi', 'yo', 'elo', 'siema'],
        ['Witam pana kierownika!', 'Uszanowanie!']
    ],
    [
        ['wino', 'winiacz', 'piwo', 'piwko', 'browar'],
        ['Alkohol?', 'Napil bym sie...']
    ],
    [
        ['chuj', 'chuju', 'burak', 'debil'],
        ['A po co zaraz tak wulgarnie?', 'Taki mocny w gebie to moze poratujesz 50gr?']
    ]
]

def decode_message(message):
    tokens = [re.sub('[^A-Za-z0-9]+', '', word.lower()) for word in message.strip().split()]
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
def run():
    if sc.rtm_connect():
        print('[.] Mietek is alive!')
        while True:
            event_list = sc.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(format_log(event))
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')


if __name__=='__main__':
    print('[.] ~MIETEK~ the chatbot v.03')
    print('[.] Booting Mietek..')
    run()