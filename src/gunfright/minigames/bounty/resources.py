import pygame


class Resources:
    background = None
    pointer = None
    money = None

    @classmethod
    def load(cls):
        cls.background = pygame.image.load('res/bounty/background.png')
        cls.pointer = pygame.image.load('res/bounty/aim.png')
        cls.money = pygame.image.load('res/bounty/money.png')
