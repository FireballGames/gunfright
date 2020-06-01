import pygame
from v2.window import Window as BaseWindow


class Window(BaseWindow):
    @classmethod
    def next_turn(cls):
        pygame.time.delay(100)
