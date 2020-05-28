"""
Gunfright game globals
"""
from d2game import states
from d2game.game import Game
from log import logger
# from .minigames.simple import Simple
# from .minigames.bountyshooter import BountyShooter
# from .minigames.seekbandit import SeekBandit
# from .player import Player
from .ui import UI


class Gunfright(Game):
    def __init__(self, config):
        super().__init__(config)

        # self.player = Player(self.config)

        self.__ui = UI(self.config)
        self.__ui.play()

    @property
    def ui(self):
        return self.__ui

    def mini_games(self):
        # yield Simple(self.player, self.config)
        yield from []
        # yield BountyShooter(self.player, self.config),
        # yield SeekBandit(self.player, self.config),
        # yield BountyShooter(self.player, self.config)

    def on_win(self):
        super().on_win()
        # self.player.levelup()
        # self.state = states.PLAY

    def on_play(self):
        super().on_play()

        logger.info("Running the game")

        self.next_level()
        for game in self.mini_games():
            # game.load_level(self.player.level)
            self.play_mini_game(game)
            if self.state != states.PLAY:
                return
            logger.debug("Next mini game")
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
