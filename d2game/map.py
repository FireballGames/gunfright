#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  map.py
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

import random


class People():
    def __init__(self, x, y):
        self.pos = [x, y]
        self.dir = 0
        self.size_x = 16
        self.size_y = 16

    def move(self, d):
        global size_x, size_y

        self.diri = d
        if d == 0:
            m = (1, 0)
        if d == 1:
            m = (0, 1)
        if d == 2:
            m = (-1, 0)
        if d == 3:
            m = (0, -1)

        n = [self.pos[0]+m[0], self.pos[1]+m[1]]

        if n[0] < 0:
            n[0] = 0
        if n[0] >= self.size_x*5:
            n[0] = self.size_x*5-1
        if n[1] < 0:
            n[1] = 0
        if n[1] >= self.size_y*5:
            n[1] = self.size_y*5-1

        t = self.map.get_tile(n[0], n[1])

        self.pos = n


class Wall():
    def __init__(self, is_passable, sprite_id):
        self.is_passable = is_passable
        self.image = sprite_id


class Building():
    def __init__(self, walls, floor=0):
        self.walls = walls
        self.floor = floor

    def get_tile(self, x=0, y=0):
        if x <= 0:
            return self.walls[0]['tiles']
        if y <= 0:
            return self.walls[1]['tiles']
        return (self.floor+10, 10)

    def is_wall(self, x=0, y=0):
        return ((x == 0) and self.walls[0]['has_exit']) or \
            ((y == 0) and self.walls[1]['has_exit'])


def draw_map(x, y, sx, sy):
    global map, people


class Map():
    def __init__(self, size):
        self.map = []

        self.generate_walls()
        self.generate_buildings()
        self.generate_map(size)

        # for i in range(random.randrange(size_x, size_x*size_y/2)):
        #   p = [random.randrange(size_x*5), random.randrange(size_y*5)]
        #   people.append(
        #       People(p[0], p[1])
        #   )

    def generate_walls(self):
        self.walls = [
            Wall(True, 0),
            Wall(False, 1),
            Wall(True, 2)
        ]

    def generate_buildings(self):
        self.buildings = [
            Building([None]*4, 0),
            Building([self.walls[1]]*4, 0)
        ]

        for i in range(4):
            b_walls = [self.walls[2]]*4
            b_walls[i] = self.walls[1]
            self.buildings.append(Building(b_walls, 1))

    def get_tile(self, x, y):
        room = self.map[int(x/5)][int(y/5)]
        in_room = (x % 5, y % 5)
        return room.get_tile(*in_room)

    def is_wall(self, x, y):
        room = self.map[int(x/5)][int(y/5)]
        in_room = (x % 5, y % 5)
        return room.is_wall(*in_room)

    def draw(self, x, y, sx, sy):
        print("Map (%s, %s)" % (x, y))
        x_begin = x - sx / 2
        x_end = x + sx / 2
        y_begin = y - sy / 2
        y_end = y + sy / 2
        print ((x_begin, x_end), (y_begin, y_end))

        rows = []
        for j in range(y-sy/2, y+sy/2+1):
            if j < 0:
                continue
            row = []
            for i in range(x-sx/2, x+sx/2+1):
                if i < 0:
                    continue

                tile = self.get_tile(i, j)[0]
                # for p in people:
                #    # if (p.pos[0] == i) and (p.pos[1] == j):
                #        # tile = '@'
                # if (bandit.pos[0] == i) and (bandit.pos[1] == j):
                #    # tile = 'B'

                if (i == x) and (j == y):
                    tile = '*'

                row.append(tile)
            print(row)
            rows.append(row)

    def generate_map(self, size):
        self.map = []

        for x in range(size[0]):
            col = []
            for y in range(size[1]):
                if self.is_border((x, y), size):
                    building = self.buildings[1]
                else:
                    if random.randrange(100) < 50:
                        building = self.buildings[0]
                    else:
                        building = self.buildings[random.randrange(len(self.buildings))]
                col.append(building)
            self.map.append(col)

    def is_border(self, pos, size):
        return (pos[0] <= 0) or (pos[0] >= size[0] - 1) or (pos[1] <= 0) or (pos[1] >= size[1] - 1)


def main():
    return 0

if __name__ == '__main__':
    main()
