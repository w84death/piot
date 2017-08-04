import config
import os

class Display:
    def __init__(self):  
        self.cfg = config.Config()        

    def draw_header(self):
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        print(title)
        return True   

    def compose_footer(self):
        footer = '[?] Wyslij wiadomosc *tablica tresc* do @mietek na firmowym Slacku!'
        return footer

    def draw_footer(self):
        print(self.compose_footer())
        return True

    def clear(self):
        os.system('clear')
        return True

    def compose_titlebar(self, title = 'WINDOW', char = '-'):
        bar = '{char}[  {title}  ]'.format(char=char, title=title)
        for i in range(0, self.cfg.get_settings('screen_width')-len(bar)):
            bar += char
        return bar

    def compose_separator(self, char = '-'):
        separator = ''
        for i in range(0, self.cfg.get_settings('screen_width')):
            separator += char
        return separator

    def compose_data_row(self, text):
        return '> {text}'.format(text=text)

    def draw_data(self, data, title, show_last):
        print(self.compose_titlebar(title, '='))

        for i in range(len(data)-show_last, len(data)):
            if i > -1 and i < len(data):
                print(self.compose_data_row(str(data[i])))
        
        print(self.compose_separator('='))
        return True