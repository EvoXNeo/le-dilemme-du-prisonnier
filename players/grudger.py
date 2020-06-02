from players.player import Player


class Grudger(Player):
    # Cooperate until the first time he's betrayed, then betray until the end 
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

    def reset(self):
        Player.reset(self)
        self.__grudge = False