class Game:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players