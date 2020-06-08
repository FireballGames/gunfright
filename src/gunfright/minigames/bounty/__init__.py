import logging
import pygame
from d2game import Game
from .pointer import Pointer
from .resources import Resources
from .shooting_range import ShootingRange


logger = logging.getLogger('gunfright.bounty')


class BountyShooter(Game):
    def __init__(
        self,
        window,
        player,
        bounds=None,
        level=0,
        timeout=5000,
        **options,
    ):
        logging.debug("Shoot money game")
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        self.bounds = bounds or pygame.Rect(0, 0, self.window.width, self.window.height)
        self.surface = pygame.Surface((self.bounds.width, self.bounds.height))
        self.rect = self.surface.get_rect()

        Resources.load()

        pygame.time.set_timer(pygame.USEREVENT, timeout)

        self.objects = pygame.sprite.LayeredUpdates()

        self.load_level(level)

        self.shooting_range = ShootingRange(self.rect, level)
        self.pointer = Pointer(self.rect)
        # self.shots = Pointer(self.rect)
        # self.lives = Pointer(self.rect)
        # self.score = Pointer(self.rect)

        self.objects.add(self.shooting_range, layer=4)
        self.objects.add(self.pointer, layer=8)

        # Set Handlers

        self.events[pygame.QUIT].append(self.__on_quit)
        self.events[pygame.KEYUP].append(self.__on_key_up)
        self.events[pygame.MOUSEMOTION].append(self.__on_mouse_move)
        self.events[pygame.MOUSEBUTTONDOWN].append(self.__on_mouse_button_down)
        self.events[pygame.USEREVENT].append(self.__on_timeout)

    def clear(self):
        self.window.surface.blit(Resources.background, (0, 0))

    def update(self):
        super().update()
        self.objects.update()

    def draw(self):
        self.objects.draw(self.surface)
        self.window.surface.blit(Resources.background, (0, 0))
        self.window.surface.blit(self.surface, self.bounds)

    def load_level(self, level):
        logging.debug("Loading level {}".format(level))

        # level_data = Config.level(level)
        # level_screen = Config.get_screen('shootmoney')
        # level_screen.update({
        #     'background': level_data["background"],
        #     'interface':  gui.i
        # })

        # if level_data['type'] == 'bounty':
        #     level_data['player'] = self.player
        #     self.level = ShootBounty(**level_data)
        # else:
        #     self.level = None

        # if not self.player.bonus:
        #     return

        # self.screen = screens.shootmoney.ShootMoney(**level_screen)
        # self.screen.init_win()

    # Handlers

    def __on_quit(self, event):
        self.window.close()

    def __on_key_up(self, event):
        if event.key == pygame.K_ESCAPE:
            self.window.close()

    def __on_mouse_move(self, event):
        self.pointer.move_to(*event.pos)

    def __on_mouse_button_down(self, event):
        if event.button == 1:
            self.shooting_range.shoot(self.pointer.rect)

    def __on_timeout(self, event):
        self.stop()
