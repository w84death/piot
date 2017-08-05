import random
class Commands:
    def __init__(self):
        self.cmds = {
            'board': {
                'cmd': 'board',
                'success': 'I wrote your message one the board :)',
                'failure': 'Not good. Message should be *more than {min}* but less than {max}* characters.'
            },
            'forecast': {
                'cmd': 'weather',
                'success': 'Right now is *{temp}*C*. Clouds *{clouds}%*. Wind *{speed} km/h*.',
                'failure': 'Can not fetch the weather for the cloud... How ironic is that?'
            }
        }

        self.psa = {
            'welcome': ['I am back...', 'Ready to work...'],
            'time': ['{time} goes by!', '{time} ...and the next hour just went away! ', 'It is a {time}!'],
            'standup': ['It is time. A Stand Up time. Or just {time}!', 'Team! Wake up and stand, it is {time} already!']
        }

        self.chat = [
            [
                ['hello', 'hi', 'witam', 'welcome', 'witaj', 'czesc', 'hi', 'yo', 'elo', 'siema'],
                ['Welcome my dear human!', 'For your service, human.', 'Hello, {mention}', 'Hello human fellow!']
            ],
            [
                ['identity'],
                ['I am a bot, chatbot.']
            ],
            [
                ['help', 'commands'],
                ['Here are available commands/messages that I can understand at the moment: `board _message_to_post_` and `weather`']
            ]
        ]

    def get_cmd(self, command):
        return self.cmds[command]

    def get_chat(self):
        return self.chat

    def get_psa(self, message):
        return random.choice(self.psa[message])

