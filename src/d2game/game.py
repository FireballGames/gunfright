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
        self.emit(events.START)

    def next(self):
        # self.draw_bg()
        # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
        # self.draw_fg()
        # self.window.draw()
        raise NotImplementedError()

    def run(self):
        """
        Run the game
        """
        self.state = states.PLAY
        self.emit(events.PLAY)

    def win(self):
        """
        Player wins the game
        """
        self.state = states.WIN
        self.emit(events.WIN)

    def loose(self):
        """
        Player looses the game
        """
        self.state = states.LOOSE
        self.emit(events.LOOSE)

    def end(self):
        """
        Player stops the game
        """
        self.emit(events.STOP)
        self.loose()

    def quit(self):
        """
        Player quits from the game
        """
        self.emit(events.QUIT)

    # Mini games processing

    @property
    def mini_games(self):
        yield from []

    def play_mini_games(self):
        mini_games = self.mini_games

        def event_processor(event_id, *args, **kwargs):
            if event_id == events.WIN:
                next_mini_game()
            else:
                self.emit(event_id, *args, **kwargs)

        def next_mini_game():
            game = next(mini_games, None)

            if game is None:
                return

            game.register_event_processor(event_processor)
            # game.load_level(self.player.level)
            game.run()
