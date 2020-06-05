import logging
import pygame
import random
# import gui
# import gui.controls
# import screens.shootmoney
# from config import Config
from d2game import Game
# from ..level import ShootBounty


logger = logging.getLogger('gunfright.bounty')


class BountyShooter(Game):
    class Resources(Game.Resources):
        def __init__(self):
            self.background = pygame.Surface((800, 600))
            self.background.fill((0, 0, 0))

            self.pointer = pygame.image.load('res/mouse.png')
            self.money = pygame.image.load('res/money.png')

    class Pointer(pygame.sprite.Sprite):
        def __init__(self, image, area, *groups):
            super().__init__(*groups)

            self.image = image
            self.rect = self.image.get_rect()
            self.area = area.inflate(-self.rect.width, -self.rect.height)

        def move_to(self, x, y):
            if not self.area.collidepoint(x, y):
                return

            self.rect.centerx = x
            self.rect.centery = y

    class Money(pygame.sprite.Sprite):
        money = pygame.sprite.Group()

        def __init__(self, image, area, *groups):
            super().__init__(*groups)
            self.image = image
            self.rect = self.image.get_rect()
            self.area = area
            self.rect.centerx = random.randrange(area.width)
            self.speed = (
                random.randint(-4, 4),
                random.randint(1, 4),
            )

        def update(self):
            self.rect = self.rect.move(*self.speed)

    def __init__(
        self,
        window,
        player,
        bounds=None,
        level=0,
        **options,
    ):
        logging.debug("Shoot money minigames")
        super().__init__(window, player)

        pygame.mouse.set_visible(False)

        self.bounds = bounds or pygame.Rect(0, 0, 800, 600)
        self.surface = pygame.Surface((self.bounds.width, self.bounds.height))

        self.objects = pygame.sprite.LayeredUpdates()
        self.pointer = self.Pointer(self.res.pointer, self.surface.get_rect())
        self.money = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        # self.screen = None
        # self.level = None

        self.objects.add(self.pointer, layer=8)

        self.load_level(level)

        # Set Handlers

        self.window.quit_handlers.append(self.stop)
        self.window.update_handlers.append(self.update)
        self.window.draw_handlers.append(self.draw)

        self.window.mouse_move_handlers.append(self.__on_mouse_move)
        self.window.mouse_button_down_handlers.append(self.__on_mouse_button_down)

        self.window.keys_handlers[pygame.K_ESCAPE] = [self.stop]

    def add_money(self):
        if len(self.money) > 5:
            return None
        if random.randrange(100) < 50:
            return None
        money = self.Money(self.res.money, self.surface.get_rect())
        self.money.add(money)

    def cleanup_money(self):
        for m in self.money:
            if not m.area.colliderect(m.rect):
                self.money.remove(m)

    def clear(self):
        self.window.surface.blit(self.res.background, (0, 0))
        pygame.draw.rect(self.surface, (0, 0, 255), self.surface.get_rect())
        # self.player.direction = None
        # self.player.frame_id = 0

    def update(self):
        # for missile in self.missiles:
        #     if self.bounds.left < missile.x < self.bounds.right:
        #         missile.next()
        #     else:
        #         self.missiles.pop(self.missiles.index(missile))

        # if self.player.is_jumping:
        #     self.player.jump()

        self.add_money()
        self.cleanup_money()
        self.money.update()

        self.objects.update()

    def draw_main(self, surface):
        pass

    def draw_shots(self, surface):
        pass

    def draw_lives(self, surface):
        pass

    def draw_score(self, surface):
        pass

    def draw(self):
        self.clear()

        # self.screen.show_image(gui.gui.surface)

        # self.controls['main'].show()
        # self.controls['shots'].show(self.player.shots)
        # self.controls['lives'].show(self.player.lives)
        # self.controls['score'].show(self.player.score)
        self.draw_main(self.surface)
        self.draw_shots(self.surface)
        self.draw_lives(self.surface)
        self.draw_score(self.surface)

        self.money.draw(self.surface)

        # for missile in self.missiles:
        #     self.draw_missile(missile)
        self.objects.draw(self.surface)

        self.window.surface.blit(self.surface, self.bounds)

    def stop(self):
        super().stop()
        if self.__on_mouse_move in self.window.mouse_move_handlers:
            self.window.mouse_move_handlers.remove(self.__on_mouse_move)
        if self.stop in self.window.quit_handlers:
            self.window.quit_handlers.remove(self.stop)
        if self.draw in self.window.draw_handlers:
            self.window.draw_handlers.remove(self.draw)
        if self.update in self.window.update_handlers:
            self.window.update_handlers.remove(self.update)

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

    def __on_mouse_move(self, event, *args, **kwargs):
        self.pointer.move_to(*event.pos)

    def __on_mouse_button_down(self, event, *args, **kwargs):
        if event.button == 1:
            for m in self.money:
                if self.pointer.rect.colliderect(m.rect):
                    self.money.remove(m)
