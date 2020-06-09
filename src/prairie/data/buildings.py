import random
from . import info, items


class Saloon:
    # 451

    class Visitor:
        def __init__(self, name, skill=None, stamina=None):
            self.name = name
            self.skill = None
            self.stamina = None
            self.payed = 0
            self.__rumors = []

        @property
        def drinks(self):
            return self.payed / 0.5

        @property
        def is_drunk(self):
            # 321
            return self.drinks > 1

        @property
        def will_fight(self):
            return False

        def rumors(self):
            yield from self.__rumors

        def tackle(self):
            # + 207
            # - 599 -> 91
            pass

        def win(self):
            pass

        def loose(self):
            pass

    class OldMan(Visitor):
        def __init__(self):
            super().__init__('Старик')
            self.__rumors = [
                info.Info("Род Волка"),
                info.Info("Род Ворона"),
                info.Info("Северный Перевал"),
                info.FoxTrail(),
            ]

        def rumors(self):
            # 508
            for rumor in self.__rumors:
                if self.drinks < 1:
                    return
                if self.drinks > 2:
                    return
                yield rumor

    class Rogers(Visitor):
        @property
        def will_fight(self):
            return self.stamina and self.stamina > 2

        @property
        def tamed(self):
            return self.stamina and self.stamina < 2

        def win(self):
            # 478 -> 91
            pass

        def loose(self):
            # 4 -> 91
            pass

    class RogersElder(Visitor):
        def __init__(self):
            super().__init__('Роджерс-старший', skill=10, stamina=8)

    class RogersYounger(Visitor):
        def __init__(self):
            super().__init__('Роджерс-младший', skill=9, stamina=8)

    class JimHarvey(Visitor):
        def __init__(self, enemies=()):
            super().__init__('Джим Харви')
            self.__enemies = enemies

        def rumors(self):
            # 178
            if not all(enemy.tamed for enemy in self.__enemies):
                return
            yield info.UncleJacobRanch()

    def __init__(self, title):
        self.title = title
        # 58
        self.__rogers = [
            self.RogersElder(),
            self.RogersYounger(),
        ]
        self.__harvey = self.JimHarvey(enemies=self.__rogers)
        self.visitors = [
            self.OldMan(),
            *[self.Visitor('Ковбой') for _ in range(random.randrange(10))],
            *self.__rogers,
            self.__harvey,
        ]

    def __str__(self):
        return 'Салун "{}"'.format(self.title)

    def exit(self):
        # 149
        self.__rogers[0].tackle()

    def fight(self):
        return self.__harvey.rumors()


class Shop:
    def __init__(self):
        self.__visited = False
        self.buying = {
            items.Nugget: 20,
            items.WolfSkin: 5,
            items.LynxSkin: 3,
            items.PumaSkin: 7,
            items.RabbitSkin: 0.5,
            items.BearSkin: 10,
            items.BisonSkin: 10,
        }
        self.selling = {
            # 325 -> 56
            items.Lasso: 1,
            items.Knife: 1.5,
            items.Matches: 0.5,
            items.Tobacco: 0.5,
            items.Ammo: 1,
            items.Beads: 0.5,
            items.Belt: 0.5,
            items.Mirror: 0.5,
            items.Spyglass: 9,  # 227 -> 325 -> 56
        }
        self.__bought = []

    def __str__(self):
        return 'Лавка'

    def visit(self):
        # 605
        if self.__visited:
            # 563
            pass
        else:
            # 47
            self.__bought = []
        self.__visited = True

    def leave(self):
        if len(self.__bought) <= 0:
            # 434 -> 56
            pass
        # 56


class Drugstore:
    def __init__(self):
        self.__visited = False
        self.buying = {}
        self.selling = {
            # 317
            items.Antidote: 1,
            items.Balm: 0.5,
            items.GoldenPanacea: 3,
            # 403 -> 505
        }
        self.__bought = []

    def __str__(self):
        return 'Аптекарь'

    def visit(self):
        # 31
        if self.__visited:
            # 165
            pass
        else:
            # 215 -> 317
            pass
        self.__visited = True

    def leave(self):
        # 255
        pass

    def rumors(self):
        if len(self.__bought) <= 0:
            return
        # 505
        yield info.Info('Комитет Бдительных')
