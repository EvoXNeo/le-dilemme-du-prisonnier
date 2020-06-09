from players.player import Player


class Simpleton(Player):
    # Always cooperate
    def __init__(self):
        Player.__init__(self)
        self.name = "Simpleton"

    def play(self, otherChoice, mistakeRate):
        if len(self.choice) == 0:
            self.choice.append('C')
        else : 
            if otherChoice == 'B':
                if self.choice[-1] == 'B':
                    self.choice.append('C')
                else :
                    self.choice.append('B')
            else :
                if self.choice[-1] == 'B':
                    self.choice.append('B')
                else :
                    self.choice.append('C')

        Player.apply_mistake_rate(self, mistakeRate)