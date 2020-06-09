import pygame
from d2game import Game
from .resources import Resources
from .sprites import MenuItem, PlayersOption, ControlsOption, StartOption


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

        self.players = PlayersOption(self.objects)
        self.controls = ControlsOption(self.objects)
        self.start = StartOption(self.objects)

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_play)

    def __next_players_option(self):
        pass

    def __on_quit(self, event):
        self.window.close()

    def __on_play(self, event):
        if event.key == pygame.K_1:
            self.players.next()
        elif event.key == pygame.K_2:
            self.controls.next()
        elif event.key == pygame.K_3:
            self.start.next()
            self.stop()
        elif event.key == pygame.K_ESCAPE:
            self.window.close()

    def draw(self):
        self.window.surface.blit(Resources.background, (0, 0))
        self.objects.draw(self.window.surface)
