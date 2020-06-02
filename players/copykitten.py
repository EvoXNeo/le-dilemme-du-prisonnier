from players.player import Player


class Copykitten(Player):
    # Start by cooperating and betray back only if the other 
    # betrays him 2 times in a row, to avoid grudge due to misinformation
    def __init__(self):
        Player.__init__(self)
        self.name = "Copykitten"
        self.__wasBetrayed = False

    def play(self, otherChoice):
        if otherChoice == 'B':
            if self.__wasBetrayed :
                self.choice.append('B')
            else:
                self.__wasBetrayed = True
                self.choice.append('C')
        else :
            if self.__wasBetrayed:
                self.__wasBetrayed = False
            self.choice.append('C')

    def reset(self):
        Player.reset(self)
        self.__wasBetrayed = False