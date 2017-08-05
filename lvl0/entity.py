import config

class Entity:
    def __init__(self, args):
        self.cfg = config.Config()
        
        name, x, y, ai, hp = args
        self.pos_x = x
        self.pos_y = y
        self.commands = [] # heap of commands to execute
        self.ap = 0 # action points
        self.hp = hp # hit points
        self.ai = ai # ai or player?
        self.last_move = (0,0)

    def get_pos(self):
        return self.pos_x, self.pos_y

    def get_color(self):
        if self.ai:
            return self.cfg.get_style('yellow')
        else:
            return self.cfg.get_style('white')
    def get_char(self):
        if self.ai:
            return self.cfg.get_settings('char_ai')
        else:
            return self.cfg.get_settings('char_player')

    def move(self, target = False):
        if not target:
            new_x, new_y = self.last_move
        else:
            new_x, new_y = target
        self.last_move = (new_x, new_y)
        self.pos_x += new_x
        self.pos_y += new_y
        self.ap += 1
        return True

    def add_command(self, command):
        self.commands.append(command)
        return True