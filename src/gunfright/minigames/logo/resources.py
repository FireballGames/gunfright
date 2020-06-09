import pygame


class Resources:
    background = None
    credits = None
    font = None
    splash = None

    @classmethod
    def load(cls):
        cls.background = pygame.Surface((256, 192))
        cls.font = pygame.font.SysFont('Arial', 32)
        cls.credits = cls.font.render('D2emon presents', False, (255, 255, 255))
        cls.splash = pygame.image.load('res/logo/logo.png')
