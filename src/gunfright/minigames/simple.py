import pygame
from v2.window import event
from v2.d2game import Game
from ..player import Player
from ..missile import Missile


import logging


logger = logging.getLogger('gunfright.simple')


def load_all(*images):
    return [pygame.image.load(image) for image in images]


class Simple(Game):
    class Resources:
        def __init__(self):
            self.frames = {
                Player.LEFT: load_all(
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                ),
                Player.RIGHT: load_all(
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                    'res/quickdraw.png',
                ),
            }
            self.stand = pygame.image.load('res/quickdraw.png')
            self.background = pygame.image.load('res/intro.png')

    def __init__(self, window, player, **config):
        logger.debug("Simple game")
        super().__init__(**config)
        self.window = window
        self.player = player
        # self.controls = {}
        # self.screen = None
        # self.level = None

        self.resources = self.Resources()

        self.min_x = 15
        self.max_x = 800 - 15 - self.player.width
        self.min_y = 15
        self.max_y = 600 - 15 - self.player.height

        self.missiles = []

    def clear(self):
        self.window.surface.blit(self.resources.background, (0, 0))
        self.player.direction = None
        self.player.frame_id = 0

    def draw_player(self, player):
        if self.player.frame_id > 25:
            self.player.frame_id = 0

        frames = self.resources.frames.get(self.player.direction, None)
        if frames:
            frame_id = self.player.frame_id // 5
            self.window.surface.blit(frames[frame_id], (player.x, player.y))
        else:
            self.window.surface.blit(self.resources.stand, (player.x, player.y))
        # pygame.draw.rect(self.window.surface, (0, 0, 255), (player.x, player.y, player.width, player.height))

        self.player.frame_id += 1

    def draw_missile(self, missile):
        pygame.draw.circle(self.window.surface, missile.color, (missile.x, missile.y), missile.r)

    def __on_left(self):
        if self.player.x > self.min_x:
            self.player.move(self.player.LEFT)

    def __on_right(self):
        if self.player.x < self.max_x:
            self.player.move(self.player.RIGHT)

    def __on_up(self):
        if self.player.is_jumping:
            return

        if self.player.y > self.min_y:
            self.player.move(self.player.UP)

    def __on_down(self):
        if self.player.is_jumping:
            return

        if self.player.y < self.max_y:
            self.player.move(self.player.DOWN)

    def __on_jump(self):
        if self.player.is_jumping:
            return

        self.player.start_jump()

    def __on_shoot(self):
        if len(self.missiles) >= 5:
            return
        self.missiles.append(Missile(
            self.player.x + self.player.width // 2,
            self.player.y + self.player.height // 2,
            5,
            (255, 0, 0),
            1 if self.player.shoot_direction == self.player.RIGHT else -1,
        ))

    def __on_close(self, *args, **kwargs):
        self.running = False

    def __on_draw(self, *args, **kwargs):
        self.clear()
        self.draw_player(self.player)
        for missile in self.missiles:
            self.draw_missile(missile)

    def __on_keys(self, keys=(), *args, **kwargs):
        handlers = {
            pygame.K_LEFT: self.__on_left,
            pygame.K_RIGHT: self.__on_right,
            pygame.K_UP: self.__on_up,
            pygame.K_DOWN: self.__on_down,
            pygame.K_SPACE: self.__on_jump,
            pygame.K_ESCAPE: self.__on_close,
            pygame.K_f: self.__on_shoot
        }

        for key, handler in handlers.items():
            if not keys[key]:
                continue
            handler()

    def next(self):
        handlers = {
            event.ON_CLOSE: self.__on_close,
            event.ON_DRAW: self.__on_draw,
            event.ON_KEYS: self.__on_keys,
        }

        self.window.next_turn()

        for missile in self.missiles:
            if self.min_x < missile.x < self.max_x:
                missile.next()
            else:
                self.missiles.pop(self.missiles.index(missile))

        if self.player.is_jumping:
            self.player.jump()

        for e in self.window.update():
            handler = handlers.get(e.event_id)
            if not handler:
                continue
            handler(*e.args, **e.kwargs)

    def run(self):
        logger.debug("Running simple game")
        while self.running:
            self.next()
