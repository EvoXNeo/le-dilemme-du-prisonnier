import player as p

class AllCooperate(p.Player):
    def __init__(self, name):
        self.name = name
    
    def play(self):
        print('test')