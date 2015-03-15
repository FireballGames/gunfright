#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  seekbandit.py
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


import d2game.game


class Game(d2game.game.Game):

    def __init__(self, player, params):
        d2game.game.Game.__init__(self, params)
        # self.map = Map()
        self.map = []
        # self.player = MyPlayer()
        self.player = player
        self.state = d2game.GAMEPLAY
        self.load_level(self.player.level)

    def play(self):
        d2game.game.Game.play(self)

        import gui
        gui.gui.clear()

        # global size_x, size_y, people, bandit

        print("Seek")
        # find = player.seek(bandit)
        # import random
        # chance = random.randrange(100)
        # find = (chance < 5)
        find = False
        # for p in people:
        #    # p.move(random.randrange(4))
        #    # if (p.pos[0]==player.pos[0])and(p.pos[1]==player.pos[1]):
        #        # print 'Hit by people'
        #        # return player.loose()
        #    # print p.pos
        # bandit.move(random.randrange(4))

        self.show_controls()

        import pygame
        pygame.display.flip()
        pygame.time.delay(2)

        if find:
            self.state = d2game.GAMEWIN

    def load_level(self, level):
        import config
        # import gunfright.level
        level_data = config.level(level)

        # global size_x, size_y, people, bandit
        map_x = 16
        map_y = 16
        size_x = map_x * 5
        size_y = map_y * 5
        self.generate_map(map_x, map_y)
        # bandit = People(random.randrange(size_x*5), random.randrange(size_y*5))

        print("Running bandit seeker")
        self.player.pos = [size_x/2, size_y/2]
        pass

    def generate_map(self, map_x, map_y):
        print("Generate map (%s x %s)" % (map_x, map_y))
        for j in range(map_y):
            row = []
            for i in range(map_x):
                import random
                row.append(random.randrange(10))
            self.map.append(row)
        return

    def draw_map(self):
        for i in range(len(self.map.map)):
            row = self.map.map[i]
            for j in range(len(row)):
                im = self.map.draw((i, j))
                if im is not None:
                    self.window.draw_image(im)
        pass

    def show_controls(self):
        # draw_map(player.pos[0], player.pos[1], 8, 8)
        print(self.map)
        print({
            'player': self.player.pos,
            'score':  self.player.score,
            'shots':  self.player.shots,
            'lives':  self.player.lives
        })
        return

    def process_events(self):
        d2game.game.Game.process_events(self)

        import pygame

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(0, -1)
        elif keys[pygame.K_DOWN]:
            self.player.move(0, 1)
        elif keys[pygame.K_LEFT]:
            self.player.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.player.move(1, 0)


def main():
    print("Gunfright game globals")
    return 0

if __name__ == '__main__':
    main()
