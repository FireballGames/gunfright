import pygame


class Resources:
    font = None
    title = None
    menu_items = []
    background = None

    @classmethod
    def load(cls):
        cls.font = pygame.font.SysFont('Arial', 16)
        cls.menu_items = {
            '1': pygame.image.load('res/menu/menu_item_1.png'),
            '2': pygame.image.load('res/menu/menu_item_2.png'),
            '3': pygame.image.load('res/menu/menu_item_3.png'),
        }
        cls.background = pygame.image.load('res/menu/menu.png')
        # cls.background = pygame.Surface((256, 192))
