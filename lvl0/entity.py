import config

class Entity:
    def __init__(self, args):
        self.cfg = config.Config()
        
        name, x, y, ai, hp = args
        self.pos_x = x
        self.pos_y = y
        self.commands = [] # heap of commands to execute
        self.max_cmds = 8
        self.ap = 0 # action points
        self.hp = hp # hit points
        self.ai = ai # ai or player?
        self.last_move = (0,0)

    def is_ai(self):
        return self.ai

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

    def move(self, wrd, target = False):
        if not target:
            new_x, new_y = self.last_move
        else:
            new_x, new_y = target
        
        if wrd.check_move((self.pos_x + new_x, self.pos_y + new_y)):
            self.last_move = (new_x, new_y)
            self.pos_x += new_x
            self.pos_y += new_y
            self.ap += 1
            return True
        else:
            return False

    def add_command(self, command, target):
        if len(self.commands) < self.max_cmds:
            self.commands.append((command, target))
            return True
        else:
            return False

    def get_commands(self):
        return self.commands

    def is_ready(self):
        return True if len(self.commands) == self.max_cmds else False

    def is_empty_commands(self):
        return True if len(self.commands) == 0 else False

    def execute_commands(self, wrd):
        if len(self.commands)>0:
            cmd, target = self.commands[0]

            if cmd == 'move':
                self.move(wrd, target)
            elif cmd == 'pass':
                pass
            del self.commands[0]
            return True
        else:
            return False