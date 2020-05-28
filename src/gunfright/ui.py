import pygame
# import gui
# import gui.controls
from d2game import ui
from log import logger


class UI(ui.UI):
    __p = None
    __i = None
    __g = None
    __screen_data = None

    def __init__(self, window, player, config):
        self.window = window
        self.player = player
        self.config = config

        # self.state = True
        # self.main_theme = None

        self.min_x = 15
        self.max_x = 800 - 15 - self.player.width
        self.min_y = 15
        self.max_y = 600 - 15 - self.player.height

        self.__init_ui()
        # gui.controls.Splash(self.config.screen('intro')).show()
        self.__init_game()
        # self.game = self.__init_game(current_game)

    def __init_ui(self):
        logger.debug("INIT GUI")
        self.__screen_data = self.config.screens

    def __init_game(self):
        # self.g = game
        # self.i = MainGui(**screen_data['gui'])
        pass

    def clear(self):
        self.window.surface.fill((0, 0, 0))

    @classmethod
    def on_before_turn(cls):
        pygame.time.delay(100)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.window.stop()

    def on_keys(self, keys):
        if keys[pygame.K_LEFT]:
            if self.player.x > self.min_x:
                self.player.move_to(-1, 0)
        if keys[pygame.K_RIGHT]:
            if self.player.x < self.max_x:
                self.player.move_to(1, 0)

        if self.player.is_jumping:
            self.player.jump()
        else:
            if keys[pygame.K_UP]:
                if self.player.y > self.min_y:
                    self.player.move_to(0, -1)
            if keys[pygame.K_DOWN]:
                if self.player.y < self.max_y:
                    self.player.move_to(0, 1)
            if keys[pygame.K_SPACE]:
                self.player.start_jump()

    def on_draw(self):
        self.clear()
        self.player.draw(self.window.surface)
        # pygame.display.flip()

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

    def play(self):
        self.window.play(
            on_event=self.on_event,
            on_keys=self.on_keys,
            on_draw=self.on_draw,
            on_quit=self.on_quit,
        )
