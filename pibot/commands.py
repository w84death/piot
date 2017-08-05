import random
class Commands:
    def __init__(self):
        self.cmds = {
            'board': {
                'cmd': 'tablica',
                'success': 'Zapisalem na tablicy :)',
                'failure': 'Wiadomosc musi byc *dluzsza niz {min}* znaki i *krotsza niz {max}* znakow.'
            },
            'forecast': {
                'cmd': 'pogoda',
                'success': 'Jest teraz *{temp} stopni Celsjusza*. Zachmurzenie *{clouds}%*. Wieje z predkoscia *{speed} km/h*.',
                'failure': 'Nie poge pobrac prognozy pogody :('
            }
        }

        self.psa = {
            'welcome': ['I am back...', 'Ready to work...'],
            'time': ['Minela godzina {time}!', '{time} Kolejna, godzina za nami! ', 'To juz {time}!'],
            'standup': ['Stand Up! czas zaczac. Jest {time}!', 'Niech druzyna powstanie do apelu o {time}!']
        }

        self.chat = [
            [
                ['hello', 'hi', 'witam', 'welcome', 'witaj', 'czesc', 'hi', 'yo', 'elo', 'siema'],
                ['Witam pana kierownika!', 'Uszanowanie!', 'Witaj, {mention}']
            ],
            [
                ['wino', 'winiacz', 'piwo', 'piwko', 'browar'],
                ['Alkohol?', 'Napil bym sie...']
            ],
            [
                ['chuj', 'chuju', 'burak', 'debil', 'idiot'],
                ['A po co zaraz tak wulgarnie?', 'Taki mocny w gebie to moze poratujesz 50gr?']
            ],
            [
                ['pearson', 'ioki', 'korpo'],
                ['Szlachta nie pracuje!', 'Korposzczury...', 'Do roboty a nie tylko te jutuby!']
            ],
            [
                ['pomoc', 'komendy', 'help'],
                ['Dostepne sa dwie komendy: `tablica _tresc_` oraz `pogoda`']
            ]
        ]

    def get_cmd(self, command):
        return self.cmds[command]

    def get_chat(self):
        return self.chat

    def get_psa(self, message):
        return random.choice(self.psa[message])
