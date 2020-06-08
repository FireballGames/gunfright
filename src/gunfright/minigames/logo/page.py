import pygame


class Page:
    def __init__(self, image, timeout=5000):
        self.image = image
        self.timeout = timeout

    def start(self):
        pygame.time.set_timer(pygame.KEYUP, self.timeout, True)

    def draw(self, surface):
        rect = surface.get_rect()
        image_rect = self.image.get_rect()
        surface.blit(
            self.image,
            (
                (rect.width - image_rect.width) // 2,
                (rect.height - image_rect.height) // 2,
            ),
        )
