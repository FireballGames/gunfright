from .dice import roll


class Character:
    def __init__(self, skill, stamina, shots=0):
        self.__skill = skill
        self.__stamina = stamina
        self.shots = 0

    @property
    def skill(self):
        return self.__skill

    @property
    def stamina(self):
        return self.__stamina

    @property
    def is_dead(self):
        return self.__stamina <= 0

    def set_skill(self, value):
        self.__skill = value

    def set_stamina(self, value):
        self.__stamina = value

    def attack(self, shoot=False):
        attack = roll(2) + self.skill
        if not shoot:
            return attack, attack
        elif self.shots > 0:
            self.shots -= 1
            return attack, attack
        else:
            return 0, attack


class Player(Character):
    __stats = {
        2: (8, 22, 8),
        3: (8, 22, 8),
        4: (8, 22, 8),
        5: (8, 22, 8),
        6: (8, 22, 8),
        7: (8, 22, 8),
        8: (8, 22, 8),
        9: (8, 22, 8),
        10: (8, 22, 8),
        11: (8, 22, 8),
        12: (8, 22, 8),
    }

    def __init__(self):
        self.__max_skill, self.__max_stamina, self.__max_charisma = self.__stats[roll(2)]
        super().__init__(self.__max_skill, self.__max_stamina, 6)
        self.__charisma = self.__max_charisma
        self.__luck = {1, 2, 3, 4, 5, 6}

        for _ in range(2):
            self.check_luck()

        self.items = []
        self.__max_items = 5
        self.__water = 2
        self.__money = 15
        self.__horse = 'Чикита'

    @property
    def charisma(self):
        return self.__charisma

    @property
    def luck(self):
        return len(self.__luck)

    @property
    def water(self):
        return self.__water

    @property
    def money(self):
        return self.__money

    @property
    def horse(self):
        return self.__horse

    def char_sheet(self):
        if self.is_dead:
            print('Игрок погиб')
        print('Ловкость: {}'.format(self.skill))
        print('Сила: {}/{}'.format(self.stamina, self.__max_stamina))
        print('Обаяние: {}'.format(self.charisma))
        print('Удача: {} ({})'.format(self.luck, ', '.join([str(i) for i in self.__luck])))
        print('Патроны: {}'.format(self.shots))
        print('В сумке:')
        if not len(self.items):
            print('\tНичего')
        for item_id, item in self.items:
            print('\t{}. {}'.format(item_id, item))
        print('Вода: {}'.format(self.water))
        print('Денег: {}$'.format(self.money))
        print('Лошадь: {}'.format(self.horse))

    def set_charisma(self, value):
        self.__charisma = value

    def decrease_stamina(self, value):
        self.set_stamina(self.stamina - value)

    def restore_stamina(self, value):
        self.set_stamina(min(self.stamina + value, self.__max_stamina))

    def check_charisma(self):
        result = roll(2) <= self.charisma
        if result:
            self.__charisma += 1
        else:
            self.__charisma -= 1
        return result

    def check_luck(self):
        value = roll()
        result = value in self.__luck
        self.__luck.discard(value)
        return result

    def restore_luck(self, value):
        self.__luck.add(value)

    def fight(self, enemy, shoot=False):
        while True:
            value = 3 if shoot else 2

            enemy_attack, enemy_defense = enemy.attack(shoot)
            player_attack, player_defense = self.attack(shoot)

            if enemy_attack > player_defense:
                print("Противник ранил игрока")
                self.decrease_stamina(value)
            else:
                print("Противник промазал")

            if player_attack > enemy_defense:
                print("Игрок ранил противника")
                enemy.decrease_stamina(value)
            else:
                print("Игрок промазал")

            if shoot and self.shots <= 0 and enemy.shots <= 0:
                print("Перестрелка окончена")
                print("Началась рукопашная")
                shoot = False

            if self.is_dead:
                print("Игрок погиб")
                return
            elif enemy.is_dead:
                print("Противник уничтожен")
                return

    def add_item(self, item):
        if len(self.items) < self.__max_items:
            print("В сумку больше ничего не поместится")
            return

        self.items.append(item)

    def drink_water(self):
        self.__water -= 1
        self.restore_stamina(2)

    def restore_water(self):
        self.__water = 2
