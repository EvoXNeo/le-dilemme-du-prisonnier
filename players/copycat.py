from players.player import Player


class Copycat(Player):
    # Start by cooperating then copy the previous move of his adversary
    def __init__(self):
        Player.__init__(self)
        self.name = "Copycat"
        self.choice = ['C']

    def play(self, otherChoice):
        if len(self.choice) != 0:
            self.choice.append(otherChoice)

    def reset(self):
        Player.reset(self)
        self.choice = ['C']