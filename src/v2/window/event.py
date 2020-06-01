ON_NEXT_TURN = 'EVENT.NEXT_TURN'
ON_CLOSE = 'EVENT.CLOSE'
ON_PYGAME = 'EVENT.PYGAME'
ON_KEYS = 'EVENT.KEYS_PRESSED'
ON_DRAW = 'EVENT.DRAW'


class Event:
    def __init__(self, event_id, *args, **kwargs):
        self.event_id = event_id
        self.args = args
        self.kwargs = kwargs
