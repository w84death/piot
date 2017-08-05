from array import array

class World:
    def __init__(self):
        self.width = 0
        self.height = 0

    def read_mapfile(self, map_name):
        file_data = open(map_name, "r")
        
        for columns in ( raw.strip().split() for raw in file_data ):  
            cmd = columns[0]
            if cmd == 'WIDTH':
                self.width = int(columns[1])
            elif cmd == 'HEIGHT':
                self.height = int(columns[1])
            elif cmd == 'MAP':
                self.map_data = [self.height]
            elif cmd == 'ENDMAP':
                print('Map loaded. {w}x{h}'.format(w=str(self.width), h=str(self.height)))
                return True
            else:
                self.map_data.append(list(cmd))
        return True
  
    def load_map(self, map_name = 'map_01.txt'):
        self.read_mapfile(map_name)
        return True

    def get_map_data(self):
        return self.map_data

    def get_map_dimensions(self):
        return self.width, self.height