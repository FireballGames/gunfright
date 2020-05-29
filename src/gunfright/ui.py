import logging
import pygame
# import gui
# import gui.controls
from d2game import ui
from . import events


logger = logging.getLogger('gunfright.ui')


class UI(ui.UI):
    __p = None
    __i = None
    __g = None
    __screen_data = None

    def __init__(self, window, player, config):
        super().__init__()

        self.window = window
        self.player = player
        self.config = config

        # self.state = True
        # self.main_theme = None

        self.__init_ui()
        # gui.controls.Splash(self.config.screen('intro')).show()
        self.__init_game()
        # self.game = self.__init_game(current_game)

    def __init_ui(self):
        logger.debug("Registering UI")
        self.__screen_data = self.config.screens
        self.window.register_event_processor(self.event_processor)

    def __init_game(self):
        # self.g = game
        # self.i = MainGui(**screen_data['gui'])
        pass

    def clear(self):
        self.window.surface.fill((0, 0, 0))

    def __on_start(self):
        self.emit(events.START)

    def __on_close(self):
        self.window.stop()

    def __on_keys(self, keys, *args, **kwargs):
        if keys[pygame.K_LEFT]:
            self.emit(events.LEFT)
        if keys[pygame.K_RIGHT]:
            self.emit(events.RIGHT)
        if keys[pygame.K_UP]:
            self.emit(events.UP)
        if keys[pygame.K_DOWN]:
            self.emit(events.DOWN)
        if keys[pygame.K_SPACE]:
            self.emit(events.JUMP)

    def __on_draw(self, *args, **kwargs):
        self.emit(events.DRAW)

        self.clear()
        self.player.draw(self.window.surface)
        # pygame.display.flip()

    def __on_win(self, *args, **kwargs):
        logger.debug("Win game")
        self.emit(events.WIN)
        # gui.win()

    def __on_loose(self, *args, **kwargs):
        logger.debug("Loose game")
        self.emit(events.LOOSE)
        # gui.loose()
        # self.game.quit()

    def __on_stop(self, *args, **kwargs):
        logger.debug("Stop game")
        self.emit(events.STOP)

    def __on_quit(self, *args, **kwargs):
        logger.debug("Quit game")
        self.emit(events.QUIT)
        self.window.quit()

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

    def draw_image(self, image, pos=(0, 0)):
        # self.window.blit(image, pos)
        pass

    def event_processor(self, event_id, *args, **kwargs):
        if event_id == events.START:
            self.__on_start()
        elif event_id == events.CLOSE:
            self.__on_close()
        elif event_id == events.KEYS:
            self.__on_keys(*args, **kwargs)
        elif event_id == events.DRAW:
            self.__on_draw(*args, **kwargs)
        elif event_id == events.WIN:
            self.__on_win(*args, **kwargs)
        elif event_id == events.LOOSE:
            self.__on_loose(*args, **kwargs)
        elif event_id == events.STOP:
            self.__on_stop(*args, **kwargs)
        elif event_id == events.QUIT:
            self.__on_quit(*args, **kwargs)
