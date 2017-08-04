import config
import os

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    BLUE =  '\033[34m'
    CYAN = '\033[0;36m'
    LIGHT_CYAN = '\033[1;36m'
    YELLOW = '\033[1;33m'


    # export COLOR_NC='\e[0m' # No Color
    # export COLOR_WHITE='\e[1;37m'
    # export COLOR_BLACK='\e[0;30m'
    # export COLOR_BLUE='\e[0;34m'
    # export COLOR_LIGHT_BLUE='\e[1;34m'
    # export COLOR_GREEN='\e[0;32m'
    # export COLOR_LIGHT_GREEN='\e[1;32m'
    # export COLOR_CYAN='\e[0;36m'
    # export COLOR_LIGHT_CYAN='\e[1;36m'
    # export COLOR_RED='\e[0;31m'
    # export COLOR_LIGHT_RED='\e[1;31m'
    # export COLOR_PURPLE='\e[0;35m'
    # export COLOR_LIGHT_PURPLE='\e[1;35m'
    # export COLOR_BROWN='\e[0;33m'
    # export COLOR_YELLOW='\e[1;33m'
    # export COLOR_GRAY='\e[0;30m'
    # export COLOR_LIGHT_GRAY='\e[0;37m'

class Display:
    def __init__(self):  
        self.cfg = config.Config()        
        
   

    def compose_footer(self):
        footer = '[?] Wyslij wiadomosc *tablica tresc* do @mietek na firmowym Slacku!'
        return footer



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
        print(color.BOLD + color.LIGHT_CYAN + self.compose_titlebar(title, '='))

        for i in range(len(data)-show_last, len(data)):
            if i > -1 and i < len(data):
                print(color.WHITE + self.compose_data_row(str(data[i])))
        
        print(color.BOLD + color.LIGHT_CYAN + self.compose_separator('='))
        return True

    def draw_header(self):
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        print(color.YELLOW + title)
        return True
    
    def draw_footer(self):
        print(color.CYAN + self.compose_footer())
        return True