import os

class Config:
    def __init__(self):
        self.settings = {
            'app_name': 'LvL0 - Pi Zero Terminal Shooter',
            'codename': 'lvlzero',
            'footer_text': 'WAIT. EXECUTING COMMANDS...',
            'version': '0.2',
            'delay': 0.5,
            'window_title_pos': 4,
            'window_title_log': 'GAME LOG',
            'window_title_world': 'BATTLEGROUND - JOIN TO FIGHT!',
            'window_rows_log': 3,
            'window_rows_board': 24,
            'board_db': 'board_db.p',
            'board_msg_len_min': 3,
            'board_msg_len_max': 140,
            'reader_enabled': False,
            'char_ai': 'R',
            'char_player': '@'
        }

        self.styles = {
            # colors
            'white': '\033[37m',
            'black': '\033[30m',
            'cyan': '\033[0;36m',
            'lightcyan': '\033[1;36m',
            'yellow': '\033[1;33m',
            # font
            'bold': '\033[1m',
            'underline': '\033[4m' 
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