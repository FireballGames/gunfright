import pygame


class Resources:
    font = None
    pages = []

    @classmethod
    def load(cls):
        cls.font = pygame.font.SysFont('Arial', 32)
        cls.pages = [
            cls.font.render('D2emon presents', False, (255, 255, 255)),
            pygame.image.load('res/logo/logo.png'),
        ]
