from players.player import Player
from players.copycat import Copycat
from players.allcheat import AllCheat

class Detective(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Detective"
        self.__actLikeCopycat = False

    def play(self, otherChoice):
        if len(self.choice) == 0:
            self.choice.append('C')
        elif len(self.choice) < 4: # analyze the behaviour of the other during the first turns 
            if 'B' == otherChoice: # if the other betray once, act like copycat after the analysis
                self.__actLikeCopycat = True
            if len(self.choice) == 1:
                self.choice.append('B')
            else:
                self.choice.append('C')         
        else :
            if self.__actLikeCopycat :
                Copycat.play(self, otherChoice)
            else :
                AllCheat.play(self, otherChoice)
