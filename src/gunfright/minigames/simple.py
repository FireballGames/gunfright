import pygame
from v2.window import event
from v2.d2game import Game


import logging


logger = logging.getLogger('gunfright.simple')


class Simple(Game):
    def __init__(self, window, player, **config):
        logger.debug("Simple game")
        super().__init__(**config)
        self.window = window
        self.player = player
        # self.controls = {}
        # self.screen = None
        # self.level = None

        self.min_x = 15
        self.max_x = 800 - 15 - self.player.width
        self.min_y = 15
        self.max_y = 600 - 15 - self.player.height

    def __on_left(self):
        if self.player.x > self.min_x:
            self.player.move_to(-1, 0)

    def __on_right(self):
        if self.player.x < self.max_x:
            self.player.move_to(1, 0)

    def __on_up(self):
        if self.player.is_jumping:
            return

        if self.player.y > self.min_y:
            self.player.move_to(0, -1)

    def __on_down(self):
        if self.player.is_jumping:
            return

        if self.player.y < self.max_y:
            self.player.move_to(0, 1)

    def __on_jump(self):
        if self.player.is_jumping:
            return

        self.player.start_jump()

    def __on_close(self, *args, **kwargs):
        self.running = False

    def __on_draw(self, *args, **kwargs):
        self.window.clear()
        self.window.draw_player(self.player)

    def __on_keys(self, keys=(), *args, **kwargs):
        handlers = {
            pygame.K_LEFT: self.__on_left,
            pygame.K_RIGHT: self.__on_right,
            pygame.K_UP: self.__on_up,
            pygame.K_DOWN: self.__on_down,
            pygame.K_SPACE: self.__on_jump,
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
