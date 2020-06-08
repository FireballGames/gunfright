import pygame
from collections import defaultdict


class Window:
    def __init__(
        self,
        title="Game",
        size=(800, 600),
        frame_rate=50,
        **options,
    ):
        self.options = options
        self.frame_rate = frame_rate

        pygame.init()

        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()

        self.running = True

        # Event Handlers

        # self.on_close = None
        # self.on_event = None

        # self.on_key_down = None
        # self.on_key_up = None
        # self.on_key_pressed = None

        # self.on_mouse_move = None
        # self.on_mouse_button_down = None
        # self.on_mouse_button_up = None

        # # self.keydown_handlers = defaultdict(list)
        # # self.keyup_handlers = defaultdict(list)
        # # self.keys_handlers = defaultdict(list)

    @classmethod
    def get_events(cls):
        for event in pygame.event.get():
            # self.event(self.on_event, event)
            # self.event(self.on_pygame.get(event.type, None), event)
            yield event
        # self.event(self.on_key_pressed, pygame.key.get_pressed())

    def update(self):
        pygame.display.update()
        self.clock.tick(self.frame_rate)

    @classmethod
    def close(cls):
        pygame.quit()
