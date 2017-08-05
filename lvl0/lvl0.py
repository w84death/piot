#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# lvl0 - Level Zero
# Proof of concept for terminal mulitplayer shooter
# For now it is a single player simulator
#
# see LICENSE file for licence
# see README.md for more info
# see CHANGELOG.md for detailed changes in each version
#
# (c) 2017 kj/P1X
#

import world
import renderer
import time
import players
import config
import sys
import select
import os

wrd = world.World()
ren = renderer.Renderer()
plr = players.Players(wrd)
cfg = config.Config()

wrd.load_map()
width, height = wrd.get_map_dimensions()

player_id = plr.player_join(('JOE', 18, 4, 0, 3))
plr.set_master_id(player_id)

plr.player_join(('ROBOT1', 7, 4, 1, 3))
plr.player_join(('ROBOT2', 30, 10, 1, 3))

game_time = 0

def exit_program():
    os.system('setterm -cursor on')
    sys.exit(0)

ren.clear()
while True:

    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            if line.strip().split()[0] == 'quit':
                exit_program()
            plr.handle_command(line)   
    else:
        ren.clear(True)
        ren.draw_header()
        ren.draw_info(plr.get_total_players(), game_time)
        ren.draw_map(width, height, 
            wrd.get_map_data(), 
            plr.get_players_data(), 
            game_time)            
        ren.draw_footer()
        plr.ai()

        time.sleep(cfg.get_settings('delay'))
        game_time += 1

