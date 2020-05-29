import logging
import pygame
from d2game import events


logger = logging.getLogger('gunfright.window')


class Window(events.EventEmitter):
    def __init__(
        self,
        title="Game",
        size=(800, 600),
        **config,
    ):
        super().__init__()
        logger.debug("Initializing Window (%s)", config)

        # Setting default values
        # flag = pygame.DOUBLEBUF

        # Loading values from args
        # # screen_data = config['screens']
        # if 'flag' in window_config:
        #     flag = window_config['flag']

        pygame.init()

        # Setting display mode
        # self.surface = pygame.display.set_mode(size, flag)
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        # if 'icon' in self.__res.args():
        #     pygame.display.set_icon(self.__res.load('icon', alpha=True))
        # if 'show_mouse' in window_config:
        #     pygame.mouse.set_visible(window_config['show_mouse'])

        # Music
        # if 'main_theme' in window_config:
        #     self.main_theme = window_config['main_theme']
        # if self.main_theme:
        #    init_sound(self.main_theme)

        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def next(self):
        pygame.time.delay(100)
        for event in pygame.event.get():
            self.emit(events.Event(events.PYGAME, event))
        self.emit(events.Event(events.KEYS, pygame.key.get_pressed()))
        self.emit(events.Event(events.DRAW))
        pygame.display.update()

    @classmethod
    def quit(cls):
        pygame.quit()

    def run(self):
        self.start()
        while self.running:
            self.next()
        self.emit(events.Event(events.QUIT))
