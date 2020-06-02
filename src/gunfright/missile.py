class Missile:
    SPEED = 8

    def __init__(self, x, y, r, color, direction):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.direction = direction
        self.speed = self.SPEED * direction

    def next(self):
        self.x += self.speed
