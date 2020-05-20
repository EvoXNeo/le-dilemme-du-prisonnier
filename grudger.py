from player import Player


class Grudger(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Grudger"

    def play(self):
        print('test')
