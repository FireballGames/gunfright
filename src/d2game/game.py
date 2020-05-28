"""
Basic game module
"""
import d2lib.reslib
import gui
from log import logger
from . import states
from .player import Player


class Game:
    def __init__(self, config):
        self.config = config
        self.state = states.GAME_OVER
        logger.info("Initializing game")

        self.resources = d2lib.reslib.Reslib()

        # self.window    = sdl_window.SDLwindow(self.screen)
        gui.res = self.resources

    @property
    def ui(self):
        raise NotImplementedError()

    @property
    def player(self):
        raise NotImplementedError()

    def mini_games(self):
        yield from []

    def run(self):
        """When game starts"""
        logger.info("Running game")
        self.state = states.PLAY
        while self.state == states.PLAY:
            self.on_play()
            # self.draw_bg()
            # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
            # self.draw_fg()
            # self.window.draw()
        return self.state

    def on_game_over(self):
        pass

    def on_play(self):
        """Game main loop"""
        self.process_events()
        # self.window.clear()

    def on_win(self):
        """When player wins the game"""
        logger.info('Player win')
        self.ui.on_win()

    def on_loose(self):
        """When player looses the game"""
        logger.info('Player loose')
        self.ui.on_loose()

    def end(self):
        """When player stops the game"""
        logger.info('Player stops')
        self.ui.on_stop()
        self.set_state(states.LOOSE)

    def quit(self):
        """When player quits from the game"""
        logger.info('Player quits')
        self.ui.on_quit()
        import sys

        sys.exit(0)

    def set_state(self, state):
        self.state = state
        self.apply_state()

    def apply_state(self):
        if self.state == states.GAME_OVER:
            self.on_game_over()
        elif self.state == states.PLAY:
            self.on_play()
        elif self.state == states.WIN:
            self.on_win()
        elif self.state == states.LOOSE:
            self.on_loose()

    def play_mini_game(self, mini_game):
        logger.debug("--------------------")
        state = mini_game.run()
        if state == states.WIN:
            self.set_state(states.PLAY)
        else:
            self.set_state(state)

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

    def process_event(self, event):
        """Process event"""
        pass
