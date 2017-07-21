#
# MIETEK ZUL BOT
# (c)2017 KJ/P1X
#

import os
import time
from random import randint
from slackclient import SlackClient

# SLACK CLIENT STUFF
TOKEN = os.environ.get('SLACK_MIETEK_TOKEN')
BOT_ID = os.environ.get('BOT_MIETEK_ID')
sc = SlackClient(TOKEN)

# SETTINGS
READ_WEBSOCKET_DELAY = 1

# COMMANDS
CMDS = [
    [
        ['witam', 'czesc', 'hi', 'yo', 'elo', 'siema'],['Witam pana kierownika!', 'Uszanowanie!']
    ],
    [
        ['wino', 'winiacz', 'piwo', 'piwko', 'browar'],['Alkohol?', 'Napil bym sie...']
    ],
    [
        ['chuju'],['A po co zaraz tak wulgarnie?', 'Taki mocny w gebie to moze poratujesz 50gr?']
    ]
]

# THE BRAIN OF MIETEK

def handle_command(command, channel):
    command = command.lower()
    
    print (command + " at " + channel)
    for cmd in CMDS:
        for cmd_code in cmd[0]:
             if command.startswith(cmd_code):
                say(cmd[1], channel)

def say(reply, channel):
    reply_message = reply[randint(0,len(reply)-1)]
    sc.api_call(
        "chat.postMessage", 
        as_user="true", 
        channel=channel, 
        text=reply_message)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and not 'bot_id' in output:
                return output['text'], output['channel']
    return None, None


# MAIN

if __name__ == "__main__":
    if sc.rtm_connect():
        print ("Mietek zyje!")
        
        while True:
            command, channel = parse_slack_output(sc.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed.")