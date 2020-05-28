class Player:
    def __init__(self, config):
        self.config = config

        self.score = 0
        self.level = 1
        self.lives = 3
        self.pos = [0, 0]
        self.dir = 0

    def level_up(self):
        self.level += 1
