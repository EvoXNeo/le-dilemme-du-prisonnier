import random

class Player:
    def __init__(self):
        self.name = ""
        self.__score = 0
        self.choice = list()

    def play(self, otherChoice, mistakeRate):
        return

    def apply_mistake_rate(self, mistake_rate):
        if int(random.random()*100) < mistake_rate :
            if self.choice[-1] == 'B':
                self.choice[-1] = 'C'
            else :
                self.choice[-1] = 'B'

    def reset(self):
        self.choice[:] = []
        return

    def __str__(self):
        return self.name

    def get_score(self):
        return self.__score

    def set_score(self, score : int):
        self.__score += score