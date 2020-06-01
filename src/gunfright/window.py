import pygame
from v2.window import Window as BaseWindow


class Window(BaseWindow):
    @classmethod
    def next_turn(cls):
        pygame.time.delay(100)

    def draw_player(self, player):
        pygame.draw.rect(self.surface, (0, 0, 255), (player.x, player.y, player.width, player.height))

    def clear(self):
        self.surface.fill((0, 0, 0))
