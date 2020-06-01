from players.player import Player


class Copycat(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Copycat"

    def play(self, otherChoice):
        if len(self.choice) == 0:
            self.choice.append('C')
        elif otherChoice == "C":
            self.choice.append('C')
        else :
            self.choice.append('B')