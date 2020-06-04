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

        self.turn_handlers = []
        self.quit_handlers = []
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.keys_handlers = defaultdict(list)
        self.mouse_move_handlers = []
        self.mouse_button_up_handlers = []
        self.mouse_button_down_handlers = []
        self.update_handlers = []
        self.draw_handlers = []

    @classmethod
    def handle_event(cls, handlers, *args, **kwargs):
        for handler in handlers:
            handler(*args, **kwargs)

    def update(self):
        self.handle_event(self.turn_handlers)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.handle_event(self.quit_handlers)
            elif e.type == pygame.KEYDOWN:
                self.handle_event(self.keydown_handlers[e.key], e)
            elif e.type == pygame.KEYUP:
                self.handle_event(self.keyup_handlers[e.key], e)
            elif e.type == pygame.MOUSEBUTTONUP:
                self.handle_event(self.mouse_button_up_handlers, e)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.handle_event(self.mouse_button_down_handlers, e)
            elif e.type == pygame.MOUSEMOTION:
                self.handle_event(self.mouse_move_handlers, e)
        keys = pygame.key.get_pressed()
        for key_id, handlers in self.keys_handlers.items():
            if keys[key_id]:
                self.handle_event(self.keys_handlers[key_id], keys)

        self.handle_event(self.update_handlers)
        self.handle_event(self.draw_handlers)

        pygame.display.update()

        self.clock.tick(self.frame_rate)

    @classmethod
    def close(cls):
        pygame.quit()
