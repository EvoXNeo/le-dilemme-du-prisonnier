from players.player import Player


class Gradual(Player):
    # Start by cooperating, when he's betrayed for the nth time, betray back for n turns
    # Then forgive for 2 turn, and so on
    def __init__(self):
        Player.__init__(self)
        self.name = "Gradual"
        self.__nbBetrayal = 0
        self.__grudgeCount = 0
        self.__isOnGrudge = False

    def play(self, otherChoice, mistakeRate):
        if self.__isOnGrudge :
            if self.__grudgeCount == 0:
                self.__grudgeCount = -2
                self.__isOnGrudge = False
                self.choice.append('C')
            else :
                self.choice.append('B')
                self.__grudgeCount -= 1
        else:  
            if otherChoice == 'B':
                if self.__grudgeCount == 0: # Betrayal during a normal cooperation
                    self.startGrudge()
                    self.choice.append('B')
                elif self.__grudgeCount < 0: # Betrayal during the 2 turns of forgiveness
                    self.__grudgeCount += 1
                    if self.__grudgeCount == 0: # If it was the last turn of forgiveness, prepare the next punition
                        self.startGrudge()
                    self.choice.append('C')
            else : # both cooperating
                if self.__grudgeCount < 0: # update the count of forgiveness turns 
                    self.__grudgeCount += 1
                self.choice.append('C')

        Player.apply_mistake_rate(self, mistakeRate)

    def startGrudge(self):
        self.__isOnGrudge = True
        self.__grudgeCount = self.__nbBetrayal
        self.__nbBetrayal += 1

    def reset(self):
        Player.reset(self)
        self.__isOnGrudge = False
        self.__nbBetrayal = 0
        self.__grudgeCount = 0