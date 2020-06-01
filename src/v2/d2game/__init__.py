class Game:
    def __init__(self, **config):
        self.config = config
        self.running = True

    def run(self):
        raise NotImplementedError()

    def quit(self):
        pass
