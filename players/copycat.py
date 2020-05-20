from players.player import Player


class Copycat(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Copycat"

    def play(self):
        print('test')