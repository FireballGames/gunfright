class Player:
    def __init__(self, config):
        self.config = config

        self.score = 0
        self.level = 1
        self.lives = 3

        self.x = 0
        self.y = 0
        self.direction = 0

    def level_up(self):
        self.level += 1
