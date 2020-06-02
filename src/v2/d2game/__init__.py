from collections import defaultdict


class Game:
    def __init__(self, window, player, **options):
        self.window = window
        self.player = player
        self.options = options
        self.running = True

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def run(self):
        raise NotImplementedError()

    def quit(self):
        pass
