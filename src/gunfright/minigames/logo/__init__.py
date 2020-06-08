import pygame
from d2game import Game
from .page import Page
from .resources import Resources


class Logo(Game):
    def __init__(
        self,
        window,
        player,
        **options,
    ):
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        Resources.load()

        self.__page_id = 0
        self.pages = list(map(Page, Resources.pages))

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_play)

    @property
    def page(self):
        if self.__page_id >= len(self.pages):
            self.stop()
            return None

        return self.pages[self.__page_id]

    def __on_quit(self, event):
        self.window.close()

    def __on_play(self, event):
        self.__page_id += 1
        if self.page is not None:
            self.page.start()

    def draw(self):
        if self.page is not None:
            self.page.draw(self.window.surface)
