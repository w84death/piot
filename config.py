import os

class Config:
    def __init__(self):
        self.settings = {
            'app_name': 'PiBot - Intranet Chatbot System',
            'codename': 'Mietek the chatbot',
            'version': '0.10',
            'delay': 0.9,
            'window_title_pos': 4,
            'window_title_log': 'LOG WINDOW',
            'window_title_board': 'WHITEBOARD',
            'board_db': 'board_db.p',
            'board_msg_len_min': 3,
            'board_msg_len_max': 140,
        }

        self.api_keys = {
            'forecast': os.environ.get('API_KEY_WEATHER'),
            'slack': os.environ.get('API_KEY_SLACK_MIETEK'),
            'bot': os.environ.get('BOT_MIETEK_ID'),
        }

    def get_settings(self, item):
        return self.settings[item]

    def get_api_key(self, api):
        return self.api_keys[api]