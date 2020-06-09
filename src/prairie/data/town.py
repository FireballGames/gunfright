from .buildings import Saloon, Shop, Drugstore


class Town:
    def __init__(self, name):
        self.name = name


class TwoPoplars(Town):
    def __init__(self):
        # 1
        super().__init__('Ту-Поппларс')
        self.places = [
            Saloon('Мустанг'),
            'Ресторан "Двери Рая"',  # 181
            'Постоялый двор',  # 382
            # 91
            Shop(),
            Drugstore(),
            # 132 -> 294
        ]
