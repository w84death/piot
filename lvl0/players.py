class Players:
    def __init__(self):
        self.players_data = []
        self.total_players = 0

    def get_player_template(self, name, x, y):
        player = {
            'name': name,
            'x': x,
            'y': y
        }
        return player

    def player_join(self, new_player):
        self.players_data.append(new_player)
        self.total_players = len(self.players_data)

    def get_players_data(self):
        return self.players_data

    def get_total_players(self):
        return self.total_players