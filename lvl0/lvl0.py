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

wrd = world.World()
ren = renderer.Renderer()
plr = players.Players()
cfg = config.Config()

wrd.load_map()
width, height = wrd.get_map_dimensions()

plr.player_join(plr.get_player_template('test', 18,4))
 
game_time = 0

while True:
    ren.clear()
    ren.draw_header()
    ren.draw_info(plr.get_total_players(), game_time)
    ren.draw_map(width, height, 
        wrd.get_map_data(), 
        plr.get_players_data(), 
        game_time)
    ren.draw_footer()

    time.sleep(cfg.get_settings('delay'))
    game_time += 1
