class Player:
    def __init__(self):
        self.name = ""
        self.__score = 0
        self.choice = list()

    def play(self, otherChoice):
        return

    def reset(self):
        self.choice[:] = []
        return

    def __str__(self):
        return self.name

    def get_score(self):
        return self.__score

    def set_score(self, score : int):
        self.__score += score