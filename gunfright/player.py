#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  player.py
#
#  Copyright 2015 Dmitry Kutsenko <d2emonium@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import d2game.player


class Player(d2game.player.Player):

    def __init__(self, config):
        d2game.player.Player.__init__(self, config)
        self.score = 250
        self.shots = 6
        self.lives = 5
        self.bonus = True

    def can_shoot(self):
        return self.shots > 0

    def shoot(self):
        if self.can_shoot():
            self.shots -= 1
            return True
        else:
            return False

    def hit_targets(self, pos=(0, 0), targets=[], delta=10):
        if not self.shoot():
            return False

        hits = []
        for target in targets:
            if (abs(pos[0] - target.pos[0]) < delta) and \
                    (abs(pos[1] - target.pos[1]) < delta):
                hits.append(target)

        print "Shot %s - %s" % (str(pos), len(hits))
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
        d2game.player.Player.levelup(self)

        import random
        chance = random.randrange(100)
        print("Chance %s vs %s" % (chance, 50))
        self.bonus = chance < 50

    def move(self, *dir):
        self.dir = dir

        self.pos[0] += dir[0]
        self.pos[1] += dir[1]

        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > 63:
            self.pos[0] = 63
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] > 63:
            self.pos[1] = 63

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


def main():
    return 0

if __name__ == '__main__':
    main()
