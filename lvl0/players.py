import entity
import random

class Players:
    def __init__(self, world):
        self.game_mode = 0
        self.wrd = world
        self.players_data = []
        self.total_players = 0
        self.commands = {
            'go': ['go', 'goto'],
            'up': ['up'],
            'left': ['le', 'left'],
            'right': ['ri', 'right'],
            'down': ['do','down'],
            'pass': ['pa', 'pass', 'idle', 'id'],
            'quit': ['q', 'quit', 'exit', 'stop'],
            'ready': ['r', 'ready', 're', 'start']
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

    def add_command(self, player, command, target = False):
        player.add_command(command, target)

    def handle_command(self, cmd):
        p = self.master_player
        cmds = cmd.strip().split()
        
        if len(cmds) > 0:
            if cmds[0] in self.commands['quit']:
                return False
            elif cmds[0] in self.commands['go']:
                if len(cmds) > 1:
                    if cmds[1] in self.commands['up']:
                        self.add_command(p, 'move', (0,-1))
                    elif cmds[1] in self.commands['right']:
                        self.add_command(p, 'move', (1,0))
                    elif cmds[1] in self.commands['down']:
                        self.add_command(p, 'move', (0,1))
                    elif cmds[1] in self.commands['left']:
                        self.add_command(p, 'move', (-1,0))
                else:
                    self.add_command(p, 'move')
                return True
            elif cmds[0] in self.commands['pass']:
                self.add_command(p, 'idle')
                return True
            elif cmds[0] in self.commands['ready']:
                if p.is_ready():
                    self.ai()
                    self.end_turn()
                return True
            else:
                return True
        else:
            return True

    def ai(self):
        for p in self.players_data:
            if p.is_ai():
                for r in range(8):
                    r = random.randint(0,10)
                    if r in (1,2,3,4):
                        target = (random.randint(-1,1), 0)
                    elif r in (5,6,7,8):
                        target = (random.randint(-1,1), 0)
                    else: 
                        target = False
                    self.add_command(p, 'move', target)

    def end_turn(self):
        self.game_mode = 1

    def start_turn(self):
        self.game_mode = 0

    def is_mode(self, mode):
        return self.game_mode == mode

    def execute_commands(self):
        run = True
        if self.is_mode(1):
            for p in self.players_data:
                if not p.execute_commands(self.wrd):
                    run = False
        return run

    def get_cmds_count(self):
        return len(self.master_player.get_commands())

    def is_master_ready(self):
        return self.master_player.is_ready()

