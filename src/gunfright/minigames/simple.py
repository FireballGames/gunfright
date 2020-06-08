import pygame
from collections import defaultdict
from d2game import Game
from ..player import Player
from ..missile import Missile


import logging


logger = logging.getLogger('gunfright.simple')


def load_all(*images):
    return [pygame.image.load(image) for image in images]


class Simple(Game):
    class Resources:
        frames = {}
        stand = None
        background = None

        @classmethod
        def load(cls):
            cls.frames = {
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
            cls.stand = pygame.image.load('res/quickdraw.png')
            cls.background = pygame.image.load('res/intro.png')

    def __init__(self, window, player, **options):
        super().__init__(window, player)
        self.objects = []
        # self.screen = None
        # self.level = None
        self.bounds = pygame.Rect(15, 15, 800 - 30, 600 - 30)
        self.missiles = []

        self.res = self.Resources()
        self.res.load()

        self.window.quit_handlers.append(self.stop)
        self.window.keydown_handlers = defaultdict(list)
        self.window.keyup_handlers = defaultdict(list)
        self.window.mouse_handlers = []
        self.window.keys_handlers = defaultdict(list)
        self.window.update_handlers.append(self.update)
        self.window.draw_handlers.append(self.draw)

        self.window.keys_handlers[pygame.K_LEFT] = [self.__on_left]
        self.window.keys_handlers[pygame.K_RIGHT] = [self.__on_right]
        self.window.keys_handlers[pygame.K_UP] = [self.__on_up]
        self.window.keys_handlers[pygame.K_DOWN] = [self.__on_down]
        self.window.keys_handlers[pygame.K_SPACE] = [self.__on_jump]
        self.window.keys_handlers[pygame.K_ESCAPE] = [self.stop]
        self.window.keys_handlers[pygame.K_f] = [self.__on_shoot]

    def clear(self):
        self.window.surface.blit(self.res.background, (0, 0))
        self.player.direction = None
        self.player.frame_id = 0

    def draw_player(self, player):
        if self.player.frame_id > 25:
            self.player.frame_id = 0

        frames = self.res.frames.get(self.player.direction, None)
        if frames:
            frame_id = self.player.frame_id // 5
            self.window.surface.blit(frames[frame_id], (player.x, player.y))
        else:
            self.window.surface.blit(self.res.stand, (player.x, player.y))
        # pygame.draw.rect(self.window.surface, (0, 0, 255), (player.x, player.y, player.width, player.height))

        self.player.frame_id += 1

    def draw_missile(self, missile):
        pygame.draw.circle(self.window.surface, missile.color, (missile.x, missile.y), missile.r)

    def __on_left(self):
        if self.player.x > self.bounds.left:
            self.player.move(self.player.LEFT)

    def __on_right(self):
        if self.player.x < self.bounds.right - self.player.width:
            self.player.move(self.player.RIGHT)

    def __on_up(self):
        if self.player.is_jumping:
            return

        if self.player.y > self.bounds.top:
            self.player.move(self.player.UP)

    def __on_down(self):
        if self.player.is_jumping:
            return

        if self.player.y < self.bounds.bottom - self.player.height:
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

    def update(self):
        for missile in self.missiles:
            if self.bounds.left < missile.x < self.bounds.right:
                missile.next()
            else:
                self.missiles.pop(self.missiles.index(missile))

        if self.player.is_jumping:
            self.player.jump()

        # for o in self.objects:
        #     o.update()
        pass

    def draw(self):
        self.clear()
        self.draw_player(self.player)
        for missile in self.missiles:
            self.draw_missile(missile)
        # for o in self.objects:
        #     o.draw(self.window.surface)
