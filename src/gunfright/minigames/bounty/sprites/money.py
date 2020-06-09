import pygame
from gunfright.minigames.bounty.resources import Resources


class Money(pygame.sprite.Sprite):
    def __init__(self, center, speed, *groups):
        super().__init__(*groups)
        self.image = Resources.money
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = speed

    def update(self):
        self.rect = self.rect.move(*self.speed)
