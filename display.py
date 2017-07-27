from asciimatics.scene import Scene
from asciimatics.screen import Screen
import config

class Display:
    def __init__(self):  
        self.cfg = config.Config()
        Screen.wrapper(self.wrapper)
        
    def draw_header(self):
        self.scr.move(0, 0)
        self.scr.draw(self.scr.width, 0, None, self.scr.COLOUR_GREEN)
        title = ' {app_name} [v{version}] '.format(
            app_name = self.cfg.get_settings('app_name'),
            version = self.cfg.get_settings('version'))
        self.scr.print_at(title, 
            self.cfg.get_settings('window_title_pos'), 0, 
            self.scr.COLOUR_GREEN, self.scr.A_BOLD)    

    def draw_footer(self):
        self.scr.print_at('[?] Wyslij wiadomosc *tablica tresc* do @mietek na firmowym Slacku!.', 
            1, self.scr.height-3, self.scr.COLOUR_YELLOW)
        self.scr.print_at('[?] (c) 2017 kj/P1X', 
            1, self.scr.height-2, self.scr.COLOUR_RED)

    def render_frame(self, title, x, y, max_x, max_y, color):
        self.scr.move(x,y)
        self.scr.draw(max_x, y, None, color)
        self.scr.draw(max_x, max_y, None, color)
        self.scr.draw(x, max_y, None, color)
        self.scr.draw(x, y, None, color)
        self.scr.print_at(' {title} '.format(title=title), 
            self.cfg.get_settings('window_title_pos'), y, 
            color, self.scr.A_BOLD)
        return True

    def draw_data(self, data, title, x, y, show_last, color):
        top_y = y
        max_x = self.scr.width
        for i in range(len(data)-show_last, len(data)):
            self.scr.move(x,y)
            self.scr.draw(max_x-1, y, ' ', self.scr.COLOUR_WHITE, color)    
            if i > -1 and i < len(data):
                self.scr.print_at(str(data[i]), x, y, self.scr.COLOUR_BLACK, 0, color)
            y += 1
        self.render_frame(title, 0, top_y, max_x-1, y, color)
        return True

    def key_check(self):
        ev = self.scr.get_key()
        if ev in (ord('Q'), ord('q')):
            #raise StopApplication("User requested exit")
            return False
        return True

    def refresh(self):
        self.scr.refresh()
        return True

   

    def get_color(self, color):
        if color == 'red':
            return self.scr.COLOUR_RED
        elif color == 'white':
            return self.scr.COLOUR_WHITE
        # default
        return self.scr.COLOUR_WHITE

    def get_height(self):
        return self.scr.height

    def wrapper(self, scr):
        self.scr = scr
        return True
    
