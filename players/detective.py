from players.player import Player
from players.copycat import Copycat
from players.allcheat import AllCheat

class Detective(Player):
    # Analyze the behaviour of the other during the first turns 
    # if the other betray once, act like copycat after the analysis
    # if not, exploit it by always betraying
    def __init__(self):
        Player.__init__(self)
        self.name = "Detective"
        self.__actLikeCopycat = False

    def play(self, otherChoice):
        if len(self.choice) == 0:
            self.choice.append('C')
        elif len(self.choice) < 4: 
            if 'B' == otherChoice: 
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

    def reset(self):
        Player.reset(self)
        self.__actLikeCopycat = False