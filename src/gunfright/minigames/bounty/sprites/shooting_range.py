import logging
import pygame
import random
from gunfright.minigames.bounty.sprites.money import Money


logger = logging.getLogger('gunfright.bounty.shooting_range')


class ShootingRange(pygame.sprite.Sprite):
    COLOR = (0, 0, 255)
    MAX_SPEED = 2

    def __init__(self, rect, level, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect

        self.background = pygame.Surface((rect.width, rect.height))
        self.background.fill(self.COLOR)

        self.money = pygame.sprite.Group()

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

    def update(self):
        self.money.update()

        for money in self.money:
            if not self.rect.colliderect(money.rect):
                self.money.remove(money)

        chance = random.randrange(100)
        if chance < 5:
            self.add_money()

        self.image.blit(self.background, (0, 0))
        self.money.draw(self.image)

    def add_money(self):
        if len(self.money) > 5:
            return None

        center = (
            random.randrange(self.rect.width),
            0,
        )
        speed = (
            random.randint(-self.MAX_SPEED, self.MAX_SPEED),
            random.randint(1, self.MAX_SPEED),
        )
        return Money(center, speed, self.money)

    def shoot(self, rect):
        for money in self.money:
            if rect.colliderect(money.rect):
                self.money.remove(money)
