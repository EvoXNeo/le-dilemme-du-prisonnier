from players.player import Player


class Copycat(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Copycat"
        self.choice = ['C']

    def play(self, otherChoice):
        if len(self.choice) != 0:
            self.choice.append(otherChoice)