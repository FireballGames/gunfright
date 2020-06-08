import pygame
from d2game import Game
from .resources import Resources


class MainMenu(Game):
    def __init__(
        self,
        window,
        player,
        **options,
    ):
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        Resources.load()

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_play)

    def __on_quit(self, event):
        self.window.close()

    def __on_play(self, event):
        print(event)
        # self.stop()

    def draw(self):
        self.window.surface.blit(Resources.background, (0, 0))
        for item_id, menu_item in enumerate(Resources.menu_items):
            self.window.surface.blit(
                menu_item.item_id,
                (
                    (8 * 11),
                    (8 * 3) + item_id * (8 * 7),
                ),
            )
            self.window.surface.blit(
                menu_item.title,
                (
                    (8 * 8),
                    (8 * 6) + item_id * (8 * 7),
                ),
            )
            self.window.surface.blit(
                menu_item.icon,
                (
                    (8 * 3),
                    (8 * 3) + item_id * (8 * 7),
                ),
            )
