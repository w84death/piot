import os

class Config:
    def __init__(self):
        self.settings = {
            'version': '0.2',
            'app_name': 'PiSocket - Telnet for sharing texts on LED banner',
            'server_ip': '192.168.1.105',
            'server_port': 4003
        }

        self.messages = {
            'recieved': b'\033[0;36;44m[i] Message recieved!\n',
            'disconnected' : b'\033[0;36;44m[-] User disconnected\n',
            'connected' : b'\033[0;36;44m[+] New user connected!\n',
            'welcome' : b'\033[0;36;44m[i] \n\n\n\n\n\n\nWelcome to the PiSocket Server!\n\nWrite something \033[37m_>',
            'chat' : b'\033[1;36;44m[.] _> ',
            'chat_reset': b'\033[0;36;44m'
        }

        self.styles = {
            # colors
            'clear': '\033[=18h\033[1;37;44m\033[0;0f',
            'white': '\033[37m',
            'black': '\033[30m',
            'info':'\033[0;30;46m'
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