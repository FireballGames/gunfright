"""
Basic game module
"""
# import d2lib.reslib
# import gui
from log import logger
from . import states


class Game:
    def __init__(self, config):
        logger.info("Initializing game")
        self.config = config
        self.__state = states.GAME_OVER

        # self.resources = d2lib.reslib.Reslib()
        # self.window    = sdl_window.SDLwindow(self.screen)
        # gui.res = self.resources

    # Properties

    @property
    def ui(self):
        raise NotImplementedError()

    @property
    def player(self):
        raise NotImplementedError()

    @property
    def is_playing(self):
        return self.state == states.PLAY

    # Event processing

    def process_event(self, event):
        """Process event"""
        pass

    def process_events(self):
        """Process game events"""
        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         logger.debug("QUIT")
        #         self.set_state(states.LOOSE)
        #     if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        #         logger.debug("ESCAPE")
        #         self.set_state(states.LOOSE)
        #     self.process_event(e)
        pass

    # Main game loop

    def next(self):
        """Game main loop"""
        self.process_events()
        # self.window.clear()

    # State handlers

    def on_game_over(self):
        pass

    def on_play(self):
        while self.is_playing:
            self.next()
            # self.draw_bg()
            # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
            # self.draw_fg()
            # self.window.draw()

    def on_win(self):
        """When player wins the game"""
        logger.info('Player win')
        self.ui.on_win()

    def on_loose(self):
        """When player looses the game"""
        logger.info('Player loose')
        self.ui.on_loose()

    # Main loop

    def run(self):
        """
        Player starts the game
        """
        logger.info("Game starts")
        self.play()
        if self.state == states.WIN:
            return states.PLAY
        else:
            return self.state

    def end(self):
        """
        Player stops the game
        """
        logger.info("Game stops")
        self.ui.on_stop()
        self.loose()

    def quit(self):
        """
        Player quits from the game
        """
        logger.info('Player quits')
        self.ui.on_quit()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
        if self.__state == states.GAME_OVER:
            self.on_game_over()
        elif self.__state == states.PLAY:
            self.on_play()
        elif self.__state == states.WIN:
            self.on_win()
        elif self.__state == states.LOOSE:
            self.on_loose()

    def game_over(self):
        self.state = states.GAME_OVER

    def play(self):
        self.state = states.PLAY

    def win(self):
        self.state = states.WIN

    def loose(self):
        self.state = states.WIN

    # Mini games processing

    @property
    def mini_games(self):
        yield from []

    def play_mini_games(self):
        for game in self.mini_games:
            logger.debug("Next mini game")
            logger.debug("--------------------")
            # game.load_level(self.player.level)
            self.state = game.play_as_mini_game()
            if not self.is_playing:
                break
