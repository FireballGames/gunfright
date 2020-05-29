import logging
from d2game import game, states
from .. import events


logger = logging.getLogger('gunfright.simple')


class Simple(game.Game):
    def __init__(self, ui, player, config):
        logger.debug("Simple game")
        super().__init__(config)

        self.__ui = ui
        self.__player = player
        # self.controls = {}
        # self.screen = None
        # self.level = None

        self.min_x = 15
        self.max_x = 800 - 15 - self.player.width
        self.min_y = 15
        self.max_y = 600 - 15 - self.player.height

        print(self.ui)
        self.__ui.register_event_processor(self.event_processor)

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
        # self.win()
        pass

    # Events

    def __process_event(self, event):
        """Process event"""
        pass

    def __on_left(self):
        logger.debug('LEFT')
        if self.player.x > self.min_x:
            self.player.move_to(-1, 0)

    def __on_right(self):
        logger.debug('RIGHT')
        if self.player.x < self.max_x:
            self.player.move_to(1, 0)

    def __on_up(self):
        logger.debug('UP')
        if self.player.is_jumping:
            return
        if self.player.y > self.min_y:
            self.player.move_to(0, -1)

    def __on_down(self):
        logger.debug('DOWN')
        if self.player.is_jumping:
            return
        if self.player.y < self.max_y:
            self.player.move_to(0, 1)

    def __on_jump(self):
        logger.debug('JUMP')
        if self.player.is_jumping:
            return
        self.player.start_jump()

    def __on_draw(self, *args, **kwargs):
        if self.player.is_jumping:
            self.player.jump()
        # self.window.clear()
        pass

    def __on_event(self, event, *args, **kwargs):
        # if event.type == pygame.QUIT:
        #     logger.debug("QUIT")
        #     self.set_state(states.LOOSE)
        # if event.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        #     logger.debug("ESCAPE")
        #     self.set_state(states.LOOSE)
        self.__process_event(event)
        pass

    def event_processor(self, event_id, *args, **kwargs):
        """
        Process game events
        """
        print(event_id, *args, **kwargs)
        if event_id == events.PYGAME:
            self.__on_event(*args, **kwargs)
        elif event_id == events.LEFT:
            self.__on_left()
        elif event_id == events.RIGHT:
            self.__on_right()
        elif event_id == events.UP:
            self.__on_up()
        elif event_id == events.DOWN:
            self.__on_down()
        elif event_id == events.JUMP:
            self.__on_jump()
        elif event_id == events.DRAW:
            self.__on_draw(*args, **kwargs)
