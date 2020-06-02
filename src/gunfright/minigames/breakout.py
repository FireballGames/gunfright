import pygame
from collections import defaultdict
from v2.d2game import Game
from v2.d2game.game_object import GameObject


class Brick(GameObject):
    def __init__(self, bounds, color, effect=None, **options):
        super().__init__(bounds, (0, 0), **options)
        self.color = color
        self.effect = effect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)


class Ball(GameObject):
    def __init__(self, x, y, r, color, speed, **options):
        super().__init__(
            (x - r, y - r, r * 2, r * 2),
            speed,
            **options,
        )
        self.r = r
        self.d = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.r)


class Paddle(GameObject):
    LEFT = 0
    RIGHT = 1

    def __init__(self, bounds, color, offset, **options):
        super().__init__(bounds, (0, 0), **options)
        self.color = color
        self.offset = offset
        self.direction = None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)


class Breakout(Game):
    class Resources:
        def __init__(self, background_filename):
            if background_filename:
                self.background = pygame.image.load(background_filename)
            else:
                self.background = None

            pygame.mixer.pre_init(44100, 16, 2, 4096)
            pygame.font.init()

    def __init__(self, window, player, **options):
        super().__init__(window, player, **options)
        self.objects = []

        self.res = self.Resources(
            background_filename=options.get('background'),
        )

        self.window.quit_handlers.append(lambda: self.window.close())
        self.window.keydown_handlers = defaultdict(list)
        self.window.keyup_handlers = defaultdict(list)
        self.window.mouse_handlers = []
        self.window.update_handlers.append(self.update)
        self.window.draw_handlers.append(self.draw)

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        self.window.surface.blit(self.res.background, (0, 0))
        for o in self.objects:
            o.draw(self.window.surface)

    def run(self):
        while self.running:
            self.window.update()
