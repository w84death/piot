import os

class Config:
    def __init__(self):
        self.settings = {
            'version': '0.1',
            'app_name': 'PiSocket - Telnet for sharing texts on LED banner',
            'server_ip': '127.0.0.1',
            'server_port': 4004
        }

        self.messages = {
            'recieved': b'[i] Message recieved!\n',
            'disconnected' : b'[-] User disconnected\n',
            'connected' : b'[+] New user connected!\n',
            'welcome' : b'[i] Welcome to the PiSocket Server!\n'
        }

        self.styles = {
            # colors
            'white': '\033[37m',
            'black': '\033[30m',
            
            'default': '\033[0;30;46m',

            'header': '\033[1;36;46m',
            'infobar':'\033[0;30;46m',
            'titlebar': '\033[1;36;40m',
            'separator': '\033[1;36;40m',
            'footer':'\033[0;30;46m',
            'input': '\033[1;36;46m',

        }

        self.api_keys = {
            'forecast': os.environ.get('API_KEY_WEATHER'),
        }

    def get_setting(self, item):
        return self.settings[item]

    def get_msg(self, item):
        return self.messages[item]

    def get_api_key(self, api):
        return self.api_keys[api]

    def get_style(self, item):
        return self.styles[item]