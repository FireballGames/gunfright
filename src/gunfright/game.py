"""
Gunfright game globals
"""
import sys
from d2game import states
from d2game.game import Game
from log import logger
# from .minigames.simple import Simple
# from .minigames.bountyshooter import BountyShooter
# from .minigames.seekbandit import SeekBandit
from .player import Player
from .ui import UI
from .window import Window


class Gunfright(Game):
    def __init__(self, config):
        super().__init__(config)

        window_config = {
            **self.config.window,
            'size': (800, 600),
            'main_theme': self.config.main_theme,
        }
        self.window = Window(**window_config)

        self.__player = Player(self.config.player or {})

        self.__ui = UI(self.window, self.__player, self.config)

    @property
    def ui(self):
        return self.__ui

    @property
    def player(self):
        return self.__player

    @property
    def mini_games(self):
        # yield Simple(self.player, self.config)
        yield from []
        # yield BountyShooter(self.player, self.config),
        # yield SeekBandit(self.player, self.config),
        # yield BountyShooter(self.player, self.config)

    def on_win(self):
        super().on_win()
        # self.player.level_up()
        # self.state = states.PLAY

    def next(self):
        super().next()

        logger.info("Running the game")

        self.ui.play()

        self.next_level()
        self.play_mini_games()
        self.shoot_bandit()
        self.win()

    def next_level(self):
        logger.debug("Next level screen")
        self.ui.next_level()

    def shoot_bandit(self):
        logger.debug("Shoot bandit minigames")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        if not self.is_playing:
           return

    def quit(self):
        super().quit()
        sys.exit(0)
