import logging
import pygame
from d2game import player


logger = logging.getLogger('gunfright.player')


class Player(player.Player):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

    def __init__(self, **options):
        super().__init__(**options)

        self.x = 400
        self.y = 300
        self.width = 40
        self.height = 60
        self.speed = 15
        self.__jump_counter = None

        self.score = 250
        self.shots = 6
        self.lives = 5
        self.bonus = True

        self.direction = None
        self.shoot_direction = self.RIGHT
        self.frame_id = 0

    @property
    def is_jumping(self):
        return self.__jump_counter is not None

    def move(self, direction):
        self.direction = direction
        if direction == self.LEFT:
            if self.x > 5:
                self.x -= self.speed
            self.shoot_direction = self.LEFT
        elif direction == self.RIGHT:
            self.direction = self.RIGHT
            if self.x < (800 - 40 - 5):
                self.x += self.speed
            self.shoot_direction = self.RIGHT
        elif direction == self.UP:
            if self.y > 5:
                self.y -= self.speed
        elif direction == self.DOWN:
            if self.y < (600 - 60 - 5):
                self.y += self.speed

    def start_jump(self):
        self.__jump_counter = 10

    def stop_jump(self):
        self.__jump_counter = None

    def jump(self):
        if not self.is_jumping:
            return

        if self.__jump_counter < -10:
            self.stop_jump()
            return

        if self.__jump_counter < 0:
            self.y += (self.__jump_counter ** 2) / 2
        else:
            self.y -= (self.__jump_counter ** 2) / 2

        self.__jump_counter -= 1

    ####

    def can_shoot(self):
        return self.shots > 0

    def shoot(self):
        if self.can_shoot():
            self.shots -= 1
            return True
        else:
            return False

    def hit_targets(self, pos=(0, 0), targets=(), delta=10):
        if not self.shoot():
            return False

        hits = []
        for target in targets:
            if (abs(pos[0] - target.pos[0]) < delta) and \
                    (abs(pos[1] - target.pos[1]) < delta):
                hits.append(target)

        print("Shot %s - %s" % (str(pos), len(hits)))
        for hit in hits:
            self.score += target.cost
            # 100
            hit.enabled = False

        return hits

    def reload(self):
        shot_cost = 10
        if self.score > shot_cost:
            self.score -= shot_cost
            self.shots = 6

    def levelup(self):
        super().levelup()

        import random
        chance = random.randrange(100)
        print("Chance %s vs %s" % (chance, 50))
        self.bonus = chance < 50

    def move_old(self, dir, map):
        logger.debug("Move event from %s to %s" % (self.pos, dir))
        logger.debug(map)

        self.dir = dir

        new_pos = map.pos_dir(self.pos, self.dir)
        logger.debug("New position will be at: %s" % (new_pos))

        logger.debug(new_pos)
        logger.debug("Before can go: %s" % (self.pos))
        if map.can_go(self.pos, self.dir):
            self.pos = new_pos
        else:
            logger.debug("Can't go")
        logger.debug("Final position: %s" % (self.pos))

        self.pos = map.patch_constraints(self.pos)
        logger.debug("After patch: %s" % (self.pos))
        logger.debug(map.map_array[self.pos[0]][self.pos[1]].tile)

    def seek(self, bandit):
        # dx = bandit.pos[0] - self.pos[0]
        # dy = bandit.pos[1] - self.pos[1]

        # if (dx == 0) and (abs(dy) < 8):
        #     return True
        # if (dy == 0) and (abs(dx) < 8):
        #     return True

        # if abs(dx) > abs(dy):
        #     if dx > 0:
        #         self.move(0)
        #     else:
        #         self.move(2)
        # else:
        #     if dy > 0:
        #         self.move(1)
        #     else:
        #         self.move(3)

        # import random
        # chance = random.randrange(100)
        # find = (chance < 5)

        return False

    def loose(self):
        self.lives -= 1
        return False
