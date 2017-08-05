import entity
import random

class Players:
    def __init__(self, world):
        self.wrd = world
        self.players_data = []
        self.total_players = 0
        self.commands = {
            'go': 'go',
            'up': 'up',
            'left': 'le',
            'right': 'ri',
            'down': 'do'
        }
        
    def player_join(self, new_player):
        self.players_data.append(entity.Entity((new_player)))
        self.total_players = len(self.players_data)
        player_id = self.total_players
        return player_id - 1

    def set_master_id(self, player_id):
        self.master_id = player_id
        self.master_player = self.players_data[player_id]
        return True

    def get_players_data(self):
        return self.players_data

    def get_total_players(self):
        return self.total_players

    def move_player(self, player, target = False):
        player.move(self.wrd, target)

    def handle_command(self, cmd):
        p = self.master_player
        cmds = cmd.strip().split()
        if len(cmds) > 0 and cmds[0] == self.commands['go']:
            if len(cmds) > 1:
                if cmds[1] == self.commands['up']:
                    self.move_player(p, (0,-1))
                elif cmds[1] == self.commands['right']:
                    self.move_player(p, (1,0))
                elif cmds[1] == self.commands['down']:
                    self.move_player(p, (0,1))
                elif cmds[1] == self.commands['left']:
                    self.move_player(p, (-1,0))
            else:
                self.move_player(p)

    def ai(self):
        for p in self.players_data:
            if p.is_ai():
                if random.randint(0,10)>5:
                    target = (random.randint(-1,1), 0)
                else:
                    target = (random.randint(-1,1), 0)
                self.move_player(p, target)