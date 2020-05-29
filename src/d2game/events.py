PYGAME = 'EVENTS.PYGAME'
KEYS = 'EVENTS.KEYS'
DRAW = 'EVENTS.DRAW'
WIN = 'EVENTS.WIN'
LOOSE = 'EVENTS.LOOSE'
STOP = 'EVENTS.STOP'
QUIT = 'EVENTS.QUIT'


class Event:
    def __init__(self, event_id, *args, **kwargs):
        self.event_id = event_id
        self.args = args
        self.kwargs = kwargs


class EventEmitter:
    def __init__(self):
        self.__processors = []

    def register_event_processor(self, processor):
        self.__processors.append(processor)

    def emit(self, event):
        for processor in self.__processors:
            processor(event)
