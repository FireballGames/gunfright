import pygame
from log import logger


class Window:
    def __init__(
        self,
        title="Game",
        size=(800, 600),
        **config,
    ):
        logger.debug("INIT WINDOW %s", config)

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

        self.running = True

    def stop(self):
        self.running = False

    @classmethod
    def next_turn(cls):
        pygame.time.delay(100)

    @classmethod
    def update(cls):
        pygame.display.update()

    @classmethod
    def quit(cls):
        pygame.quit()

    def play(
        self,
        on_event=lambda event: None,
        on_keys=lambda keys: None,
        on_draw=lambda: None,
        on_quit=lambda: None,
    ):
        while self.running:
            self.next_turn()
            for event in pygame.event.get():
                on_event(event)
            on_keys(pygame.key.get_pressed())
            on_draw()
            self.update()
        on_quit()
