import pygame


class TextObject(pygame.sprite.Sprite):
    def __init__(
        self,
        text,
        rect,
        font,
        color=(255, 255, 255),
        *groups,
    ):
        super().__init__(*groups)

        self.text = text

        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.font = font
        self.color = color

        self.rect = rect

    def get_image(self):
        return self.font.render(self.text, False, self.color)

    def update(self):
        self.image = self.get_image()

    def draw(self, surface, center=False):
        rect = self.image.get_rect()
        if center:
            pos = (
                self.rect.left - rect.width // 2,
                self.rect.top,
            )
        else:
            pos = (
                self.rect.left,
                self.rect.top,
            )
        surface.blit(self.image, pos)
