#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MALINOWY BOT
# (C) P1X/kj
#

from blessed import Terminal
from config import Config
from twit import Twit
import os

class App:
    def __init__(self):
        self.cfg = Config()
        self.t = Terminal()
        self.tw = Twit(
            self.cfg.key('consumer_key'),
            self.cfg.key('consumer_secret'),
            self.cfg.key('access_token'),
            self.cfg.key('access_token_secret'))
        
        self.name = self.cfg.get('name')
        self.color_a = self.cfg.get('color_a')
        self.color_b = self.cfg.get('color_b')
        self.last_message = self.cfg.msg('footer').format(
            a = self.t.color(self.color_a),
            b = self.t.color(self.color_b),
            quit = self.t.underline('quit'))
        

    def colorize(self, key, message = False):
        return self.cfg.msg(key).format(
            a = self.t.color(self.color_a),
            b = self.t.color(self.color_b),
            message = message)

    def decode(self, message):
        msg = message.strip().split()
        cmd_color = ['color', 'c']
        cmd_twit = ['twit', 't']
        cmd_help = ['help', 'h']
        cmd_name = ['name']

        # COLOR
        if msg[0] in cmd_color and len(msg) == 3:

            if msg[1].isdigit() and msg[2].isdigit():
                self.color_a = int(msg[1])
                self.color_b = int(msg[2])
                return self.colorize('done')
            return self.colorize('error')
        
        # TWIT
        elif msg[0] in cmd_twit and len(msg) > 1:
        
            ret = self.tw.twit(message.replace(msg[0], '').strip())
            if ret:
                return self.colorize('twit', ret)
            else:
                return self.colorize('error')

        # NAME
        elif msg[0] in cmd_name and len(msg) > 1:
            self.name = '  {name}  '.format(
                name = message.replace(msg[0], '').strip())
            return self.colorize('done')
        
        # DEFAULT
        else:
            return self.colorize('error')

    def terminal(self):
        os.system('clear')
        with self.t.location(4, 2):
            print(self.cfg.msg('title').format(
                    a = self.t.color(self.color_a),
                    b = self.t.color(self.color_b),
                    title = self.t.underline(self.name),
                    ver = self.cfg.get('version')
                )
            )
        
        if self.last_message:
            with self.t.location(4, self.t.height - 2):
                print(self.last_message)

        with self.t.location(4, self.t.height - 4):
            message = input(self.colorize('prompt'))
            
        if message == 'quit':
            return False
        else:
            self.last_message = self.decode(message)
            return True
        

if __name__=='__main__':
    a = App()

    while a.terminal():
        pass