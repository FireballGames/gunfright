"""
Gunfright game globals
"""
import gui
import gui.controls

from d2game import states
from d2game.game import Game, UI
from log import logger
from .minigames.bountyshooter import BountyShooter
from .minigames.seekbandit import SeekBandit
from .player import Player


class D2UI(UI):
    def __init__(self, current_game, config):
        self.game = current_game
        self.config = config

        gui.init_gui(self.config)
        gui.controls.Splash(self.config.screen('intro')).show()
        gui.init_game(self.game)

    def win(self):
        gui.win()

    def loose(self):
        gui.loose()
        self.game.quit()

    def next_level(self):
        screen = gui.controls.Splash(self.config.screen('nextlev'))
        screen.controls["text"] = gui.controls.ControlText(
            "Level %s",
            pos=(100, 100),
            size=32,
        )
        screen.controls["text"].prepare(self.game.player.level)
        screen.show()


class Gunfright(Game):
    def __init__(self, config):
        super().__init__(config)

        self.player = Player(self.config)
        self.ui = D2UI(self, self.config)

        self.subgames = [
            # BountyShooter(self.player, self.config),
            SeekBandit(self.player, self.config),
            BountyShooter(self.player, self.config)
        ]

    def on_win(self):
        super().on_win()
        self.player.levelup()
        self.state = states.PLAY

    def on_play(self):
        super().on_play()

        logger.info("Running the game")

        self.next_level()
        for i in range(len(self.subgames)):
            self.subgames[i].load_level(self.player.level)
            self.play_mini_game(i)
            if self.state != states.PLAY:
                return
            logger.debug("Next minigames")
        self.shoot_bandit()
        self.set_state(states.WIN)

        logger.debug("State: %s", self.state)
        logger.debug("--------------------")

    def next_level(self):
        logger.debug("Next level screen")
        self.ui.next_level()

    def shoot_bandit(self):
        logger.debug("Shoot bandit minigames")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        if self.state != states.PLAY:
           return
