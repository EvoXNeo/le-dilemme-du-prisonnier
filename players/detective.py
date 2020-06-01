from players.player import Player


class Detective(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Detective"

    def play(self):
        print('test')
