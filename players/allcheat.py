from players.player import Player


class AllCheat(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "AllCheat"

    def play(self, otherChoice):
        self.choice.append('B')
