"""
Basic game module
"""
import pygame
import d2lib.reslib
import gui
from log import logger
from . import states
from .player import Player


class UI:
    def win(self):
        logger.debug("Win game")

    def loose(self):
        logger.debug("Loose game")

    def stop(self):
        logger.debug("Stop game")

    def quit(self):
        logger.debug("Quit game")


class Game:
    def __init__(self, config):
        self.config = config
        self.state = states.GAME_OVER
        logger.info("Initializing game")

        self.resources = d2lib.reslib.Reslib()
        self.ui = None
        self.games = []

        # self.window    = sdl_window.SDLwindow(self.screen)
        gui.res = self.resources

        self.player = Player(config)

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

    def on_game_over(self):
        pass

    def on_play(self):
        """Game main loop"""
        self.process_events()
        # self.window.clear()

    def on_win(self):
        """When player wins the game"""
        logger.info('Player win')
        if self.ui is not None:
            self.ui.win()

    def on_loose(self):
        """When player looses the game"""
        logger.info('Player loose')
        if self.ui is not None:
            self.ui.loose()

    def end(self):
        """When player stops the game"""
        logger.info('Player stops')
        if self.ui is not None:
            self.ui.stop()
        self.set_state(states.LOOSE)

    def quit(self):
        """When player quits from the game"""
        logger.info('Player quits')
        if self.ui is not None:
            self.ui.quit()
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

    def play_mini_game(self, index):
        if index not in range(len(self.games)):
            return False

        self.games[index].run()
        self.state = self.games[index].state
        if self.state == states.LOOSE:
            self.set_state(states.LOOSE)
        if self.state == states.WIN:
            self.state = states.PLAY
        print("--------------------")

        return True

    def process_events(self):
        """Process game events"""
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                logger.debug("QUIT")
                self.set_state(states.LOOSE)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                logger.debug("ESCAPE")
                self.set_state(states.LOOSE)
            self.process_event(e)

    def process_event(self, event):
        """Process event"""
        pass
