import pygame
# import gui
# import gui.controls
from d2game import game
from log import logger


class UI(game.UI):
    __p = None
    __i = None
    __g = None
    __screen_data = None

    def __init__(self, config):
        self.config = config

        # self.state = True
        # self.main_theme = None
        self.window_size = [800, 600]

        self.__init_ui()
        self.window = self.__init_window()
        # gui.controls.Splash(self.config.screen('intro')).show()
        self.__init_game()
        # self.game = self.__init_game(current_game)

    def __init_ui(self):
        logger.debug("INIT GUI")
        self.__screen_data = self.config.screens

    def __init_window(self):
        logger.debug("INIT WINDOW")
        window_config = self.config.window
        window_config.update({
            'main_theme': self.config.main_theme
        })
        logger.debug(window_config)

        # Setting default values
        # flag = pygame.DOUBLEBUF

        # Loading values from args
        # # screen_data = config['screens']
        # if 'size' in window_config:
        #     self.screen_size = window_config['size']
        # if 'flag' in window_config:
        #     flag = window_config['flag']
        # title = window_config['title']

        pygame.init()

        # Setting display mode
        # self.surface = pygame.display.set_mode(self.screen_size, flag)
        window = pygame.display.set_mode(self.window_size)

        # Other window options
        # if 'title' in window_config:
        #     pygame.display.set_caption(title)
        # if 'icon' in self.__res.args():
        #     pygame.display.set_icon(self.__res.load('icon', alpha=True))
        # if 'show_mouse' in window_config:
        #     pygame.mouse.set_visible(window_config['show_mouse'])

        # Music
        # if 'main_theme' in window_config:
        #     self.main_theme = window_config['main_theme']
        # if self.main_theme:
        #    init_sound(self.main_theme)

        return window

    def __init_game(self):
        # self.g = game
        # self.i = MainGui(**screen_data['gui'])
        pass

    def on_win(self):
        logger.debug("Win game")
        # gui.win()
        pass

    def on_loose(self):
        logger.debug("Loose game")
        # gui.loose()
        # self.game.quit()
        pass

    def on_stop(self):
        logger.debug("Stop game")

    def on_quit(self):
        logger.debug("Quit game")

    def next_level(self):
        # screen = gui.controls.Splash(self.config.screen('nextlev'))
        # screen.controls["text"] = gui.controls.ControlText(
        #     "Level %s",
        #     pos=(100, 100),
        #     size=32,
        # )
        # screen.controls["text"].prepare(self.game.player.level)
        # screen.show()
        pass

    def clear(self):
        # self.window.fill((0, 0, 0))
        pass

    def draw_image(self, image, pos=(0, 0)):
        # self.window.blit(image, pos)
        pass

    def draw(self):
        # pygame.display.flip()
        pass
