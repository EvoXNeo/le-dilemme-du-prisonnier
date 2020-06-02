from players.player import Player


class AllCooperate(Player):
    # Always cooperate
    def __init__(self):
        Player.__init__(self)
        self.name = "AllCooperate"

    def play(self, otherChoice):
        self.choice.append('C')
