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
import logging

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3

MOVES = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)

RET_DIR = (
    DIR_DOWN,
    DIR_LEFT,
    DIR_UP,
    DIR_RIGHT,
)


class Wall():
    def __init__(self, is_passable, sprite_id):
        self.is_passable = is_passable
        self.image = sprite_id

    def __repr__(self):
        if self.is_passable:
            return "0"
        else:
            return "-"


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


class Place():
    def __init__(self, tile):
        self.tile = tile
        self.walls = [Wall(True, 0)]*4

    def can_go(self, dir):
        return self.walls[dir].is_passable

    def show_walls(self):
        return (self.walls[3].is_passable * 8) + (self.walls[2].is_passable * 4) + (self.walls[1].is_passable * 2) + self.walls[0].is_passable


class MapBlock():
    def __init__(self, tile):
        self.map_array = [[Place(tile) for i in range(4)] for j in range(4)]

    def set_walls(self, walls):
        for i in range(4):
            self.map_array[0][i].walls[DIR_LEFT] = [walls[2], walls[1]][i == 1]
            self.map_array[3][i].walls[DIR_RIGHT] = [walls[2], walls[1]][i == 1]
            self.map_array[i][0].walls[DIR_UP] = [walls[2], walls[1]][i == 1]
            self.map_array[i][3].walls[DIR_DOWN] = [walls[2], walls[1]][i == 1]


class Map():
    def __init__(self, size):
        self.map = []

        map_tpl = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.map_array = [[Place(0) for i in range(64)] for j in range(64)]
        self.map_blocks = [[MapBlock(map_tpl[j][i]) for i in range(16)] for j in range(16)]

        logging.debug("Map initialization")
        self.generate_walls()
        self.generate_buildings()
        self.generate_map(size)
        self.fill_map_tpl(map_tpl)

        # for i in range(random.randrange(size_x, size_x*size_y/2)):
        #   p = [random.randrange(size_x*5), random.randrange(size_y*5)]
        #   people.append(
        #       People(p[0], p[1])
        #   )

    def fill_map_tpl(self, tpl):
        for row in range(len(tpl)):
            tpl_row = tpl[row]
            for col in range(len(tpl_row)):
                self.map_blocks[col][row].set_walls(self.walls)

                if (col in (0, 15)) or (row in (0, 15)):
                    self.set_border(col * 4, row * 4)
                elif not tpl[row][col]:
                    logging.debug("Building at %s" % ([col, row]))
                    self.set_building(col * 4, row * 4, 1)

        for row in range(64):
            st = ""
            for col in range(32):
                st += "%s," % (self.map_array[row][col].show_walls())
            logging.debug(st)

    def set_border(self, x, y):
        for i in range(4):
            for j in range(4):
                t = Place(1)
                t.walls = [self.walls[1]] * 4
                self.map_array[x + i][y + j] = t
        for i in range(len(self.map_array)):
            self.map_array[4][i].walls[DIR_LEFT] = self.walls[1]
            self.map_array[59][i].walls[DIR_RIGHT] = self.walls[1]
            self.map_array[i][4].walls[DIR_UP] = self.walls[1]
            self.map_array[i][59].walls[DIR_DOWN] = self.walls[1]

    def set_building(self, x, y, tile):
        walls = [0] * 4
        for i in range(4):
            for j in range(4):
                walls = [int(j == 0), int(i == 3), int(j == 3), int(i == 0)]
                if (i == 0) and (j == 2):
                    walls[3] = 1
                if (i == 3) and (j == 2):
                    walls[1] = 1
                if (j == 0) and (i == 2):
                    walls[0] = 1
                if (j == 3) and (i == 2):
                    walls[2] = 1
                t = Place(tile)
                for w in range(len(walls)):
                    t.walls[w] = self.walls[walls[i]]
                self.map_array[x + i][y + j] = t
            if x > 0:
                self.map_array[x - 1][y + i].walls[DIR_RIGHT] = self.walls[1]
            if x < 63:
                self.map_array[x + 1][y + i].walls[DIR_LEFT] = self.walls[1]
            if y > 0:
                self.map_array[x + i][y - 1].walls[DIR_RIGHT] = self.walls[1]
            if y < 63:
                self.map_array[x + i][y + 1].walls[DIR_LEFT] = self.walls[1]

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

    def patch_constraints(self, pos):
        constraints = ((0, 63), (0, 63))
        for i in range(2):
            if pos[i] < constraints[i][0]:
                pos[i] = constraints[i][0]
            elif pos[i] > constraints[i][1]:
                pos[i] = constraints[i][1]
        return pos

    def can_go(self, pos, dir):
        for j in range(pos[1] + 1):
            st = ""
            for i in range(pos[0] + 1):
                st += "%s," % (self.map_array[i][j].show_walls())
            logging.debug(st)

        room = self.map_array[pos[0]][pos[1]]
        logging.debug("From: %s(%s)[%s]" % (room.show_walls(), pos, room.walls))
        if room.walls[dir].is_passable:
            new_pos = self.pos_dir(pos, dir)
        else:
            return False

        constraints = ((0, 63), (0, 63))
        for i in range(2):
            if new_pos[i] not in range(*constraints[i]):
                return False

        return True
        room = self.map_array[new_pos[0]][new_pos[1]]
        logging.debug("To: %s" % (room.walls))
        return room.walls[RET_DIR[dir]].is_passable

    def pos_dir(self, pos, dir):
        new_pos = pos[:]
        for i in range(len(pos)):
            new_pos[i] += MOVES[dir][i]
        return new_pos

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
