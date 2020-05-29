"""
Gunfright game globals
"""
import logging
import sys
# from d2game import states
from d2game.game import Game
from . import events
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

        self.register_event_processor(self.event_processor)
        self.register_event_processor(self.ui.event_processor)
        self.ui.register_event_processor(self.event_processor)

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

        # self.process_events()
        # self.window.clear()

        self.next_level()
        self.play_mini_games()
        self.shoot_bandit()
        self.win()

    def start(self):
        logger.info("Gunfright starts")
        super().start()
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

    def __on_play(self):
        logger.info("Gunfright runs")
        self.play_mini_games()
        while self.is_playing:
            pass

    def __on_quit(self):
        logger.info("Gunfright stops")
        self.quit()

    def event_processor(self, event_id, *args, **kwargs):
        """
        Process game events
        """
        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         logger.debug("QUIT")
        #         self.set_state(states.LOOSE)
        #     if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        #         logger.debug("ESCAPE")
        #         self.set_state(states.LOOSE)
        #     self.process_event(e)
        print(event_id, *args, **kwargs)
        if event_id == events.PLAY:
            self.__on_play()
        if event_id == events.QUIT:
            self.__on_quit()
