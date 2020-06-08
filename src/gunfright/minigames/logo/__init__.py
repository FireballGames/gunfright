import pygame
from d2game import Game


class Logo(Game):
    class Resources(Game.Resources):
        def __init__(self):
            self.background = pygame.image.load('res/logo/logo.png')

    def __init__(
        self,
        window,
        player,
        **options,
    ):
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        self.events[pygame.QUIT].append(self.__quit)
        self.events[pygame.KEYUP].append(self.__play)

    def __quit(self, event):
        self.window.close()

    def __play(self, event):
        self.stop()

    def clear(self):
        self.window.surface.blit(self.res.background, (0, 0))

    def draw(self):
        self.clear()
