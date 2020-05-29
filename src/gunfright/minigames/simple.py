import logging
from d2game import states
from d2game.game import Game


logger = logging.getLogger('gunfright.simple')


class Simple(Game):
    def __init__(self, ui, player, config):
        logger.debug("Simple game")
        super().__init__(config)

        self.__ui = ui
        self.__player = player
        # self.controls = {}
        # self.screen = None
        # self.level = None

        self.__ui.window.register_event_processor(self.process_events)

    @property
    def ui(self):
        return self.__ui

    @property
    def player(self):
        return self.__player

    def run(self):
        logger.debug("Running simple game")
        super().run()
        return states.LOOSE

    def next(self):
        self.win()

    # Event processing

    def process_event(self, event):
        """Process event"""
        pass

    def process_events(self, event):
        """Process game events"""
        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         logger.debug("QUIT")
        #         self.set_state(states.LOOSE)
        #     if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        #         logger.debug("ESCAPE")
        #         self.set_state(states.LOOSE)
        #     self.process_event(e)
        # self.window.clear()
        pass
