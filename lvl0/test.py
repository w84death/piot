#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

WIDTH = 80
HEIGHT = 24
TIMEOUT = 100

if __name__ == '__main__':
    curses.initscr()
    curses.beep()
    curses.beep()

    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)

    pad = curses.newpad(22, 77)

    curses.noecho()
    curses.curs_set(0)
    window.border(0)
    window.addstr(0, 2, 'ASCII TERMINAL',curses.A_REVERSE)
        
    i=0
    while True:
        #window.clear()
        #window.border(0)
        pad.clear()
        for y in range(0, 22):
            for x in range(0, 77):
                try:
                    pad.addch(y,x, x+y+i)
                except curses.error:
                    pass
        pad.refresh(0,0, 2,2, 22,77)
        i = i + 1 if i < 255 else 0

        event = window.getch()
        if event == 27:
            break

    
    curses.endwin()
    curses.echo()
    curses.curs_set(1)