import pygame
# import gui
# import gui.controls
from d2game import game
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


class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 60
        self.speed = 15
        self.jumping = False
        self.jump_count = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def move(self, x, y):
        if x < 0:
            if self.x > 5:
                self.x -= self.speed
        if x > 0:
            if self.x < (800 - 40 - 5):
                self.x += self.speed
        if y < 0:
            if self.y > 5:
                self.y -= self.speed
        if y > 0:
            if self.y < (600 - 60 - 5):
                self.y += self.speed

    def start_jump(self):
        self.jumping = True
        self.jump_count = 10

    def stop_jump(self):
        self.jumping = False
        self.jump_count = 0

    def jump(self):
        if self.jump_count < -10:
            self.stop_jump()
            return

        if self.jump_count < 0:
            self.y += (self.jump_count ** 2) / 2
        else:
            self.y -= (self.jump_count ** 2) / 2

        self.jump_count -= 1


class UI(game.UI):
    __p = None
    __i = None
    __g = None
    __screen_data = None

    def __init__(self, config):
        self.config = config
        window_config = {
            **self.config.window,
            'size': (800, 600),
            'main_theme': self.config.main_theme,
        }

        # self.state = True
        # self.main_theme = None

        self.player = Player()
        self.min_x = 15
        self.max_x = 800 - 15 - self.player.width
        self.min_y = 15
        self.max_y = 600 - 15 - self.player.height

        self.__init_ui()
        self.window = Window(**window_config)
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
                self.player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            if self.player.x < self.max_x:
                self.player.move(1, 0)

        if self.player.jumping:
            self.player.jump()
        else:
            if keys[pygame.K_UP]:
                if self.player.y > self.min_y:
                    self.player.move(0, -1)
            if keys[pygame.K_DOWN]:
                if self.player.y < self.max_y:
                    self.player.move(0, 1)
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
