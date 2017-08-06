import config
import os

class Display:
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
        print(self.cfg.get_style('clear'))
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

    def compose_data_row(self, text):
        return '> {text}'.format(text=text)

    def draw_data(self, data, title, show_last, text_color):
        print(self.cfg.get_style('bold') + self.cfg.get_style('lightcyan') + self.compose_titlebar(title))

        for i in range(len(data)-show_last, len(data)):
            if i > -1 and i < len(data):
                print(text_color + self.compose_data_row(str(data[i])))
        
        print(self.cfg.get_style('bold') + self.cfg.get_style('cyan') + self.compose_separator())
        return True

    def draw_header(self):
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        print(self.cfg.get_style('yellow') + title)
        return True
    
    def draw_footer(self):
        print(self.cfg.get_style('cyan') + self.compose_footer())
        return True