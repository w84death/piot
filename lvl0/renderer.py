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

    def clear(self):
        os.system('clear')
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
        info = '/ HP: {hp}/{hp_max} / SCORE: {score} // PLAYERS: {players}/{max_players} // GAME TURN: {turn} ///'.format(
            players=str(players).zfill(2),
            max_players = 16,
            turn = str(game_time).zfill(6),
            hp = 3,
            hp_max = 3,
            score = str(int(game_time*0.25)).zfill(6))
        return info

    def compose_data_row(self, text):
        return '> {text}'.format(text=text)

    def draw_header(self):
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        print(self.cfg.get_style('yellow') + title)
        return True
    
    def draw_footer(self):
        print(self.cfg.get_style('cyan') + self.compose_footer())
        return True

    def draw_info(self, players, game_time):
        print(self.cfg.get_style('cyan') + self.compose_info(players, game_time))
        return True

    def draw_map(self, width, height, map_data, players_data, game_time): 
        
        

        print('{font}{color}{bar}'.format(
            font = self.cfg.get_style('bold'), 
            color = self.cfg.get_style('lightcyan'), 
            bar = self.compose_titlebar(self.cfg.get_settings('window_title_world'))))

        for y in range(1, height-1):
            for x in range(1, width-1):
                ent = False
                for p in players_data:
                    pos_x, pos_y = p.get_pos()
                    if pos_x == x and pos_y == y:
                        print('{color}{char}{color_reset}'.format(
                            color = p.get_color(), 
                            char = p.get_char(),
                            color_reset = self.cfg.get_style('cyan')
                        ), end='')
                        ent = True
                if not ent:
                    print('{color}{map}'.format(
                        color = self.cfg.get_style('cyan'),
                        map = map_data[y][x]), end='')
            print('')

        print('{color}{bar}'.format(
            color = self.cfg.get_style('cyan'),
            bar = self.compose_separator()))
