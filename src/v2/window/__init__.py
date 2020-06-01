import pygame
from . import event


class Window:
    def __init__(
        self,
        title="Game",
        size=(800, 600),
        **config,
    ):
        self.config = config

        pygame.init()

        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.running = True

    @classmethod
    def update(cls):
        yield event.Event(event.ON_NEXT_TURN)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                yield event.Event(event.ON_CLOSE)
            yield event.Event(event.ON_PYGAME, e)
        yield event.Event(event.ON_KEYS, pygame.key.get_pressed())
        yield event.Event(event.ON_DRAW)
        pygame.display.update()

    @classmethod
    def close(cls):
        pygame.quit()
