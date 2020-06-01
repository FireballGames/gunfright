"""
Gunfright game globals
"""
import logging
# from d2game import states
# from d2game.game import Game
from . import events
from .minigames.simple import Simple
# from .minigames.bountyshooter import BountyShooter
# from .minigames.seekbandit import SeekBandit
from .player import Player
from .window import Window


logger = logging.getLogger('gunfright')


class Gunfright:
    def __init__(self, config):
        logger.info("Initializing Gunfright")

        self.config = config
        window_config = {
            **self.config.window,
            'size': (800, 600),
            'main_theme': self.config.main_theme,
        }
        player_config = self.config.player or {}

        self.window = Window(**window_config)
        self.player = Player(**player_config)
        # self.ui = UI(self.window, self.player, self.config)

    @property
    def mini_games(self):
        logger.info("Next Mini Game")
        yield Simple(self.window, self.player)
        # yield Simple(self.ui, self.player, **self.config)
        # yield BountyShooter(self.player, **self.config),
        # yield SeekBandit(self.player, **self.config),
        # yield BountyShooter(self.player, **self.config)

    def next(self):
        logger.info("Next Gunfright Loop")

        self.next_level()
        # self.play_mini_games()
        self.shoot_bandit()
        self.win()

    def win(self):
        logger.info('Player win Gunfright')
        # self.player.level_up()
        # self.state = states.PLAY

    def loose(self):
        logger.info('Player loose Gunfright')

    def quit(self):
        logger.info('Player quits Gunfright')
        self.window.close()
        # sys.exit(0)

    def next_level(self):
        logger.debug("Next Gunfright level")
        # self.ui.next_level()

    def shoot_bandit(self):
        logger.debug("Shoot bandit minigames")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        # if not self.is_playing:
        #    return

    def __on_play(self):
        logger.info("Gunfright runs")
        # self.play_mini_games()
        # while self.is_playing:
        #     pass

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

    def run(self):
        for game in self.mini_games:
            game.run()
