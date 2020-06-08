import pygame
from d2game import Game
from .resources import Resources


class Logo(Game):
    TIMEOUT = 5000

    def __init__(
        self,
        window,
        player,
        **options,
    ):
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        Resources.load()

        pygame.time.set_timer(pygame.USEREVENT, self.TIMEOUT)

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_play)
        self.events[pygame.USEREVENT].append(self.__on_play)

    def __on_quit(self, event):
        self.window.close()

    def __on_play(self, event):
        self.stop()

    def clear(self):
        self.window.surface.blit(Resources.background, (0, 0))

    def draw(self):
        self.clear()
