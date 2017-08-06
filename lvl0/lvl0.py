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

wrd.load_map('map_02.txt')
width, height = wrd.get_map_dimensions()

plr.set_master_id(plr.player_join(('HUMAN', 28, 12, 0, 3)))

plr.player_join(('ROBOT1', 7, 4, 1, 1))
plr.player_join(('ROBOT2', 40, 12, 1, 1))
plr.player_join(('ROBOT3', 70, 8, 1, 1))
plr.player_join(('ROBOT4', 60, 9, 1, 1))
plr.player_join(('ROBOT5', 70, 10, 1, 1))


game_time = 0

def exit_program():
    os.system('setterm -cursor on')
    sys.exit(0)

def prompt_player():
    if not plr.is_master_ready():
        return input(ren.compose_player_input(True, plr.get_cmds_count(), 8))
    else:
        return input(ren.compose_player_input(False))

ren.clear()
while True:

    ren.clear(True)
    ren.draw_header()
    ren.draw_info(plr.get_total_players(), game_time)
    ren.draw_map(width, height, 
        wrd.get_map_data(), 
        plr.get_players_data(), 
        game_time)            
    ren.draw_footer()
    
    if plr.is_mode(0):
        if not plr.handle_command(prompt_player()):
            exit_program()
        ren.clear()
    elif plr.is_mode(1):
        if plr.execute_commands():
            time.sleep(cfg.get_settings('delay'))
            game_time += 1
        else:
            plr.start_turn()
