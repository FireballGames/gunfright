import pygame
from ..resources import Resources


class Centered(pygame.sprite.Sprite):
    def __init__(self, image, rect, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = rect.center


class Credits(Centered):
    def __init__(self, rect, *groups):
        super().__init__(Resources.credits, rect, *groups)
        self.timeout = 1000


class Splash(Centered):
    def __init__(self, rect, *groups):
        super().__init__(Resources.splash, rect, *groups)
        self.timeout = 1000
