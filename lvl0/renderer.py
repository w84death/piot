from __future__ import print_function
import config
import os

class Renderer:
    def __init__(self):  
        self.cfg = config.Config()        
        self.columns, self.rows = self.get_dimensions()
    
    def get_dimensions(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns), int(rows)

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows

    def compose_footer(self):
        footer = '// {body} //'.format(body = self.cfg.get_settings('footer_text'))
        return footer

    def clear(self, fast = False):
        print(self.cfg.get_style('default'))
        if not fast:
            os.system('clear')
            os.system('setterm -cursor off')
        else:
            print("\033[0;0f")
        return True

    def compose_titlebar(self, title = 'WINDOW', char = '~'):
        pos = self.cfg.get_settings('window_title_pos')
        bar = ''
        for i in range(0, pos):
            bar += '{char}'.format(char=char)
        bar += '[  {title}  ]'.format(char=char, title=title)
        for i in range(0, self.get_columns() - len(bar) - 2):
            bar += char
        bar = '+{body}+'.format(body=bar)
        return bar

    def compose_separator(self, char = '~'):
        separator = ''
        for i in range(0, self.get_columns() - 2):
            separator += char
        separator = '+{body}+'.format(body=separator)
        return separator

    def compose_info(self, players, game_time):
        info = '{color}/ HP: {hp}/{hp_max} / SCORE: {score} // PLAYERS: {players}/{max_players} // GAME TURN: {turn} ///'.format(
            color=self.cfg.get_style('infobar'),
            players=str(players).zfill(2),
            max_players = 16,
            turn = str(game_time).zfill(6),
            hp = 3,
            hp_max = 3,
            score = str(int(game_time*0.25)).zfill(6))
        return info

    def compose_player_input(self, input_commands, cmds = False, cmds_max = False):
        if input_commands:
            inp = self.cfg.get_settings('prompt_0_text').format(
                color=self.cfg.get_style('input'),
                no=str(cmds).zfill(2),
                max=str(8).zfill(2))
        else:
            inp = self.cfg.get_settings('prompt_1_text').format(
                color=self.cfg.get_style('input'))
        return inp

    def compose_data_row(self, text):
        return '> {text}'.format(text=text)

    def draw_header(self):
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        print(self.cfg.get_style('header') + title)
        return True
    
    def draw_footer(self):
        print(self.cfg.get_style('footer') + self.compose_footer())
        return True

    def draw_info(self, players, game_time):
        print(self.cfg.get_style('infobar') + self.compose_info(players, game_time))
        return True

    def draw_map(self, width, height, map_data, players_data, game_time): 
        # TITLEBAR
        print('{color}{titlebar}'.format(
            color = self.cfg.get_style('titlebar'), 
            titlebar = self.compose_titlebar(self.cfg.get_settings('window_title_world'))))

        # THE MAP
        for y in range(1, height-1):
            for x in range(1, width-1):
                for p in players_data:
                    # PLAYERS
                    if p.get_pos() == ((x, y)):
                        print('{color}{char}{color_reset}'.format(
                            color = p.get_color(), 
                            char = p.get_char(),
                            color_reset = self.cfg.get_style('cyan')
                        ), end='')
                        break
                # TERRAIN
                else:
                    print('{color}{map}'.format(
                        color = self.cfg.get_style(map_data[y][x]),
                        map = map_data[y][x]), end='')
            print('')

        # SEPARATOR/FOOTER
        print('{color}{separator}'.format(
            color = self.cfg.get_style('separator'),
            separator = self.compose_separator()))

        return True