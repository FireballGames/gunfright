import pygame
from ..resources import Resources


class MenuItem(pygame.sprite.Sprite):
    X_OFFSET = 8 * 3
    Y_OFFSET = 8 * 3
    WIDTH = 8 * 26
    HEIGHT = 8 * 7

    class ItemId(pygame.sprite.Sprite):
        def __init__(self, text, color, *groups):
            super().__init__(*groups)
            self.image = Resources.font.render(text, False, color)
            self.rect = self.image.get_rect()
            self.rect.left = (8 * 5)
            self.rect.top = (8 * 3)

    class Title(pygame.sprite.Sprite):
        def __init__(self, text, color, *groups):
            super().__init__(*groups)
            self.image = Resources.font.render(text, False, color)
            self.rect = self.image.get_rect()
            self.rect.left = (8 * 8)
            self.rect.top = (8 * 0)

            self.text = text
            self.color = color

        def update(self):
            self.image = Resources.font.render(self.text, False, self.color)

    class Icon(pygame.sprite.Sprite):
        def __init__(self, image, *groups):
            super().__init__(*groups)
            self.image = image
            self.rect = self.image.get_rect()

    def __init__(
        self,
        item_id,
        value,
        labels,
        *groups,
        id_color=(255, 255, 255),
        title_color=(255, 255, 255),
    ):
        super().__init__(*groups)

        self.default = value
        self.__value = value
        self.labels = labels or {}

        self.rect = pygame.Rect(
            self.X_OFFSET,
            self.Y_OFFSET,
            self.WIDTH,
            self.HEIGHT
        )
        self.image = pygame.Surface((self.rect.width, self.rect.height))

        self.item_id = self.ItemId(item_id, id_color)
        self.title = self.Title(self.label, title_color)
        self.icon = self.Icon(Resources.menu_items[item_id])

        self.objects = pygame.sprite.Group(
            self.item_id,
            self.title,
            self.icon,
        )

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value not in self.labels.keys():
            self.__value = self.default
        else:
            self.__value = value

    @property
    def label(self):
        return self.labels.get(self.value, '')

    def next(self):
        self.value += 1

    def clear(self):
        self.image.fill((0, 0, 0))

    def update(self):
        self.title.text = self.label
        self.objects.update()

        self.clear()
        self.objects.draw(self.image)
