class Item:
    name = ''

    BAG = 1
    KNIFE = 2
    SADDLE = 3

    @property
    def placement(self):
        return self.BAG

    def use(self, user):
        return lambda p: p


class Nugget(Item):
    name = 'Золотой Слиток'


class WolfSkin(Item):
    name = 'Шкура Волка'


class LynxSkin(Item):
    name = 'Шкура Рыси'


class PumaSkin(Item):
    name = 'Шкура Пумы'


class RabbitSkin(Item):
    name = 'Шкура Кролика'


class BearSkin(Item):
    name = 'Шкура Медведя'


class BisonSkin(Item):
    name = 'Шкура Бизона'


class Lasso(Item):
    name = 'Лассо'

    @property
    def placement(self):
        return self.SADDLE


class Knife(Item):
    name = 'Нож'

    @property
    def placement(self):
        return self.KNIFE


class Matches(Item):
    name = 'Спички'


class Tobacco(Item):
    name = 'Табак'


class Ammo(Item):
    name = 'Патроны x6'


class Beads(Item):
    name = 'Бусы'


class Belt(Item):
    name = 'Пояс'


class Mirror(Item):
    name = 'Зеркало'


class Spyglass(Item):
    name = 'Подзорная труба'

    def use(self, user):
        return lambda p: p - 30


class Drugs(Item):
    def __init__(self, count):
        self.__count = count

    @property
    def count(self):
        return self.__count

    @property
    def empty(self):
        return self.count > 0

    def effect(self, user):
        return lambda p: p

    def use(self, user):
        if self.empty:
            return lambda p: p
        self.__count -= 1
        return self.effect(user)


class Antidote(Item):
    name = 'Противоядие'

    def __init__(self):
        super().__init__(1)

    def effect(self, user):
        user.poisoned = False
        return lambda p: p


class Balm(Item):
    name = 'Бальзам'

    def __init__(self):
        super().__init__(2)

    def effect(self, user):
        user.heal_wounds(5)
        return lambda p: p


class GoldenPanacea(Item):
    name = '"Золотая Панацея"'

    def __init__(self):
        super().__init__(1)

    def effect(self, user):
        user.restore_stamina()
        return lambda p: p
