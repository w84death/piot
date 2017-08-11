import os
import curses

class Config:
    def __init__(self):
        self.settings = {
            'version': '0.2',
            'name': 'ma:/:linowy//bot',
            'prompt_size': 144,
            'color_a': 14,
            'color_b': 15,
            'background_char': '/'
        }

        self.messages = {
            'title': '{a} /// {b}{title}{a} // ver. {ver} / ',
            'prompt': '{a} /// {b}wri:{a} // :te_ / {b}',
            'footer': '{a} /// follow me {b}@MalinowyBot{a} // {quit}{a} to exit program / ',
            'loading': '{a} /// wa: // :it___ /',
            'twit': '{a} /// {b}twi:{a} // :ted / {b}{message} / ',
            'done': '{a} /// {b}do:{a} // :ne_ / ',
            'error': '{a} /// {b}err:{a} // :or_ / '
        }

        self.api_keys = {
            'consumer_key': os.environ.get('API_KEY_TWITTER_CONSUMER_KEY'),
            'consumer_secret': os.environ.get('API_KEY_TWITTER_CONSUMER_SECRET'),
            'access_token': os.environ.get('API_KEY_TWITTER_ACCESS_TOKEN'),
            'access_token_secret': os.environ.get('API_KEY_TWITTER_ACCESS_TOKEN_SECRET')
        }

    def get(self, item):
        return self.settings[item]

    def msg(self, item):
        return self.messages[item]

    def key(self, api):
        return self.api_keys[api]
