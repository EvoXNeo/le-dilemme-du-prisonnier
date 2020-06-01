from players.player import Player


class Grudger(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Grudger"
        self.__grudge = False

    def play(self, otherChoice):
        if len(self.choice) == 0 :
            self.choice.append('C')
        else :
            if otherChoice == 'B':
                self.__grudge = True
        if self.__grudge:
            self.choice.append('B')
        else :
            self.choice.append('C')

