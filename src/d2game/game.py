"""
Basic game module
"""
# import d2lib.reslib
# import gui
from . import events, states


class Game(events.EventEmitter):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.state = states.INIT

        # self.resources = d2lib.reslib.Reslib()
        # self.window    = sdl_window.SDLwindow(self.screen)
        # gui.res = self.resources

    @property
    def player(self):
        raise NotImplementedError()

    @property
    def is_playing(self):
        return self.state == states.PLAY

    def start(self):
        """
        Player starts the game
        """
        self.state = states.START

    def next(self):
        raise NotImplementedError()

    def run(self):
        """
        Run the game
        """
        self.start()
        self.state = states.PLAY
        while self.is_playing:
            self.next()
            # self.draw_bg()
            # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
            # self.draw_fg()
            # self.window.draw()
        return self.state

    def win(self):
        """
        Player wins the game
        """
        self.state = states.WIN
        self.emit(events.Event(events.WIN))

    def loose(self):
        """
        Player looses the game
        """
        self.state = states.LOOSE
        self.emit(events.Event(events.LOOSE))

    def end(self):
        """
        Player stops the game
        """
        self.emit(events.Event(events.STOP))
        self.loose()

    def quit(self):
        """
        Player quits from the game
        """
        self.emit(events.Event(events.QUIT))

    # Mini games processing

    @property
    def mini_games(self):
        yield from []

    def play_mini_games(self):
        for game in self.mini_games:
            # game.load_level(self.player.level)
            state = game.run()
            if state != states.WIN:
                self.state = state
                return
            else:
                self.state = states.PLAY
