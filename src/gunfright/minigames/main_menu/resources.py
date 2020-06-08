import pygame


class Resources:
    background = None

    @classmethod
    def load(cls):
        cls.background = pygame.image.load('res/logo/logo.png')
