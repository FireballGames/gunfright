import pygame


class TextObject:
    def __init__(
        self,
        x,
        y,
        text_func,
        color,
        font_name,
        font_size,
        **options,
    ):
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)

        self.__surface = self.get_surface(self.text_func())

    def get_surface(self, text):
        return self.font.render(text, False, self.color)

    def draw(self, surface, center=False):
        self.__surface = self.get_surface(self.text_func())
        bounds = self.__surface.get_rect()
        if center:
            pos = (
                self.pos[0] - bounds.width // 2,
                self.pos[1],
            )
        else:
            pos = self.pos
        surface.blit(self.__surface, pos)

    def update(self):
        pass
