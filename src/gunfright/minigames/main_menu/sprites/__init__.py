from .menu_item import MenuItem


class PlayersOption(MenuItem):
    ONE_PLAYER = 0
    TWO_PLAYERS = 1

    def __init__(self, *groups):
        super().__init__(
            '1',
            self.ONE_PLAYER,
            {
                self.ONE_PLAYER: 'ONE PLAYER GAME',
                self.TWO_PLAYERS: 'TWO PLAYERS GAME',
            },
            id_color=(255, 255, 255),
            title_color=(255, 0, 0),
            *groups,
        )


class ControlsOption(MenuItem):
    KEYBOARD = 0
    CURSOR = 1
    KEMPSTON = 2
    SINCLAIR = 3

    def __init__(self, *groups):
        super().__init__(
            '2',
            self.KEYBOARD,
            {
                self.KEYBOARD: 'KEYBOARD',
                self.CURSOR: 'CURSOR',
                self.KEMPSTON: 'KEMPSTON',
                self.SINCLAIR: 'SINCLAIR',
            },
            id_color=(255, 255, 0),
            title_color=(255, 0, 255),
            *groups,
        )
        self.rect = self.rect.move(0, self.HEIGHT)


class StartOption(MenuItem):
    START = 0

    def __init__(self, *groups):
        super().__init__(
            '3',
            self.START,
            {
                self.START: 'START GAME',
            },
            id_color=(0, 255, 0),
            title_color=(255, 255, 255),
            *groups,
        )
        self.rect = self.rect.move(0, self.HEIGHT * 2)
