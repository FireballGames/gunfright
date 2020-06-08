"""
Basic game module
"""
# import d2lib.reslib
# import gui
from collections import defaultdict


class Game:
    class Resources:
        def __init__(self):
            # self.resources = d2lib.reslib.Reslib()
            pass

    def __init__(self, window, player):
        # self.state = states.INIT
        self.window = window  # sdl_window.SDLwindow(self.screen)
        self.player = player
        self.res = self.Resources()  # self.resources
        self.events = defaultdict(list)
        self.running = True

    def update(self):
        for event in self.window.get_events():
            for handler in self.events[event.type]:
                handler(event)

    def draw(self):
        pass

    def stop(self):
        self.running = False

    def run(self):
        # self.state = states.PLAY
        # self.emit(events.PLAY)
        while self.running:
            self.update()
            self.draw()
            self.window.update()

    # @property
    # def is_playing(self):
    #     return self.state == states.PLAY

    # def start(self):
    #     self.state = states.START
    #     self.emit(events.START)

    # def next(self):
    #     # self.draw_bg()
    #     # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
    #     # self.draw_fg()
    #     # self.window.draw()
    #     raise NotImplementedError()

    # def win(self):
    #     self.state = states.WIN
    #     self.emit(events.WIN)

    # def loose(self):
    #     self.state = states.LOOSE
    #     self.emit(events.LOOSE)
