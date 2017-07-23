from time import localtime, strftime
import config
import commands
import filesystem

class Whiteboard:
    def __init__(self):
        self.fs = filesystem.Filesystem()
        self.cfg = config.Config()
        self.cmds = commands.Commands()
        self.board = self.fs.load()

    def get_board(self):
        return self.board

    def write(self, message, psa=False):
        if not message:
            return False

        template = '{time} {message}'
        if psa:
            template_frame = '      ***'
            template = '      *** {message}'

        t = strftime("%H:%M", localtime())
        message = message.replace(self.cmds.get_cmd('board')['cmd'], '').strip()
        message_to_save = template.format(
            time=t, 
            message=message)
    
        ml = len(message_to_save)
        if ml > self.cfg.get_settings('board_msg_len_min') and ml < self.cfg.get_settings('board_msg_len_max'):
            if psa:
                self.board.append(template_frame)
            self.board.append(message_to_save)
            if psa:
                self.board.append(template_frame)
            self.fs.save(self.board)
            return self.cmds.get_cmd('board')['success']
        else:
            return self.cmds.get_cmd('board')['failure'].format(
                min = self.cfg.get_settings('board_msg_len_min'),
                max = self.cfg.get_settings('board_msg_len_max'))
