import pygame
from d2game import Game
from .resources import Resources
from .sprites import Credits, Splash


class Logo(Game):
    PAGE_TIMEOUT = pygame.USEREVENT + 1

    def __init__(
        self,
        window,
        player,
        **options,
    ):
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        Resources.load()

        self.pages = [
            Credits(self.window.surface.get_rect()),
            Splash(self.window.surface.get_rect()),
        ]
        self.__page_id = None
        self.show()

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_play)
        self.events[self.PAGE_TIMEOUT].append(self.__on_play)

    @property
    def page(self):
        if self.__page_id is None:
            return None
        if self.__page_id >= len(self.pages):
            return None
        return self.pages[self.__page_id]

    def show(self):
        pygame.time.set_timer(self.PAGE_TIMEOUT, 0)

        if self.__page_id is None:
            self.__page_id = 0
        else:
            self.objects.remove(self.page)
            self.__page_id += 1

        if self.__page_id >= len(self.pages):
            self.stop()
            return None

        self.objects.add(self.page)
        pygame.time.set_timer(self.PAGE_TIMEOUT, self.page.timeout)

    def __on_quit(self, event):
        self.window.close()

    def __on_play(self, event):
        self.show()

    def draw(self):
        self.window.surface.blit(Resources.background, (0, 0))
        self.objects.draw(self.window.surface)
