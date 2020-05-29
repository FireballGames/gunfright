"""
Gunfright game globals
"""
import logging
import sys
# from d2game import states
from d2game.game import Game
from .minigames.simple import Simple
# from .minigames.bountyshooter import BountyShooter
# from .minigames.seekbandit import SeekBandit
from .player import Player
from .ui import UI
from .window import Window


logger = logging.getLogger('gunfright')


class Gunfright(Game):
    def __init__(self, config):
        logger.info("Initializing Gunfright")
        super().__init__(config)

        window_config = {
            **self.config.window,
            'size': (800, 600),
            'main_theme': self.config.main_theme,
        }
        self.window = Window(**window_config)

        self.__player = Player(self.config.player or {})

        self.ui = UI(self.window, self.__player, self.config)
        self.register_event_processor(self.ui.event_processor)

    @property
    def player(self):
        return self.__player

    @property
    def mini_games(self):
        logger.info("Next Mini Game")
        yield Simple(self.ui, self.player, self.config)
        # yield BountyShooter(self.player, self.config),
        # yield SeekBandit(self.player, self.config),
        # yield BountyShooter(self.player, self.config)

    def next(self):
        logger.info("Next Gunfright Loop")

        self.process_events()
        # self.window.clear()

        self.next_level()
        self.play_mini_games()
        self.shoot_bandit()
        self.win()

    def run(self):
        logger.info("Gunfright starts")
        super().run()
        self.window.run()

    def win(self):
        logger.info('Player win Gunfright')
        super().win()
        # self.player.level_up()
        # self.state = states.PLAY

    def loose(self):
        logger.info('Player loose Gunfright')
        super().loose()

    def end(self):
        logger.info("Gunfright stops")
        super().end()

    def quit(self):
        logger.info('Player quits Gunfright')
        super().quit()
        sys.exit(0)

    def next_level(self):
        logger.debug("Next Gunfright level")
        self.ui.next_level()

    def shoot_bandit(self):
        logger.debug("Shoot bandit minigames")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        # if not self.is_playing:
        #    return

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
