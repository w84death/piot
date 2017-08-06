import os

class Config:
    def __init__(self):
        self.settings = {
            'version': '0.5',
            'app_name': 'LvL0 - Pi Zero Terminal Shooter',
            'codename': 'lvlzero',
            'footer_text': 'COMMANDS: GO UP/RI/DO/LE, READY/HELP/QUIT',
            'prompt_0_text': '{color}[PHASE 00] FILL UP TO {max} COMMANDS. ENTER COMMAND {no}: ',
            'prompt_1_text': '{color}[PHASE 01] TYPE READY TO START: ',
            'delay': 0.5,
            'window_title_pos': 4,
            'window_title_world': 'BATTLEGROUND - PLAN YOUR MOVES WISELY!',
            'char_ai': 'R',
            'char_player': '@'
        }

        self.styles = {
            # colors
            'white': '\033[37m',
            'black': '\033[30m',
            'cyan': '\033[0;30;46m',
            'lightcyan': '\033[1;36m',
            'yellow': '\033[1;33m',
            # font
            'bold': '\033[1m',
            'underline': '\033[4m',

            'header': '\033[0;30;43m',
            'infobar':  '\033[0;36;46m',

            '@': '\033[0;37;42m',
            '.': '\033[0;32;42m',
            '#': '\033[0;30;42m',
            '_': '\033[0;34;44m',
            'V': '\033[0;30;43m'
        }

        self.api_keys = {
            'forecast': os.environ.get('API_KEY_WEATHER'),
            'slack': os.environ.get('API_KEY_SLACK_PIBOTZERO'),
            'bot': os.environ.get('BOT_ID_PIBOTZERO'),
        }

    def get_settings(self, item):
        return self.settings[item]

    def get_api_key(self, api):
        return self.api_keys[api]

    def get_style(self, item):
        return self.styles[item]