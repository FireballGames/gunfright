import pygame
from gunfright.minigames.bounty.resources import Resources


class Pointer(pygame.sprite.Sprite):
    def __init__(self, area, *groups):
        super().__init__(*groups)

        self.image = Resources.pointer
        self.rect = self.image.get_rect()
        self.area = area.inflate(-self.rect.width, -self.rect.height)

    def move_to(self, x, y):
        if not self.area.collidepoint(x, y):
            return

        self.rect.centerx = x
        self.rect.centery = y
