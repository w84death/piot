import os

class Config:
    def __init__(self):
        self.settings = {
            'app_name': 'PIBOT ZERO - Intranet Chatbot System ',
            'codename': 'mietek',
            'footer_text': 'Just chat with the bot :) Send message *help* to @pibotzero on the company Slack!',
            'version': '0.14.3',
            'delay': 0.9,
            'screen_width': 80,
            'window_title_pos': 4,
            'window_title_log': 'SLACK NETWORK LOG',
            'window_title_board': 'WHITEBOARD - WRITE WHATEVER YOU WANT',
            'window_rows_log': 3,
            'window_rows_board': 24,
            'board_db': 'board_db.p',
            'board_msg_len_min': 3,
            'board_msg_len_max': 140,
            'reader_enabled': False
        }

        self.styles = {
            # colors
            'clear': '\033[1;30;47m',
            'white': '\033[0;30;47m',
            'black': '\033[1;37;40m',
            'cyan': '\033[0;34;47m',
            'lightcyan': '\033[1;34;47m',
            'yellow': '\033[1;33;47m',
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