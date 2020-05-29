PYGAME = 'EVENTS.PYGAME'
KEYS = 'EVENTS.KEYS'
DRAW = 'EVENTS.DRAW'
START = 'EVENTS.START'
PLAY = 'EVENTS.PLAY'
WIN = 'EVENTS.WIN'
LOOSE = 'EVENTS.LOOSE'
STOP = 'EVENTS.STOP'
QUIT = 'EVENTS.QUIT'
CLOSE = 'EVENTS.CLOSE'


class EventEmitter:
    def __init__(self):
        self.__processors = []

    def register_event_processor(self, processor):
        self.__processors.append(processor)
        print(self, self.__processors)

    def emit(self, event_id, *args, **kwargs):
        for processor in self.__processors:
            processor(event_id, *args, **kwargs)
