import pygame


class MenuItem:
    def __init__(self, item_id, title, icon):
        self.item_id = item_id
        self.title = title
        self.icon = icon


class Resources:
    font = None
    title = None
    menu_items = []
    background = None

    @classmethod
    def load(cls):
        cls.font = pygame.font.SysFont('Arial', 16)
        cls.menu_items = [
            MenuItem(
                cls.font.render('ONE PLAYER GAME', False, (255, 0, 0)),
                cls.font.render('1', False, (255, 255, 255)),
                pygame.image.load('res/menu/menu_item_1.png'),
            ),
            MenuItem(
                cls.font.render('KEYBOARD', False, (255, 0, 255)),
                cls.font.render('2', False, (255, 255, 0)),
                pygame.image.load('res/menu/menu_item_2.png'),
            ),
            MenuItem(
                cls.font.render('START GAME', False, (255, 255, 255)),
                cls.font.render('3', False, (0, 255, 0)),
                pygame.image.load('res/menu/menu_item_3.png'),
            ),
        ]
        cls.background = pygame.image.load('res/menu/menu.png')
        # cls.background = pygame.Surface((256, 192))
