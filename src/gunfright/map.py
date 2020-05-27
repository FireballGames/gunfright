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

import d2game.map

map_tpl = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map(d2game.map.Map):
    def __init__(self):
        d2game.map.Map.__init__(self)

        self.map_from_tpl()

        import sdl_sprite
        self.image = sdl_sprite.SDLSprite('res/border.png', (24, 24))
        pass

    def draw(self, pos):
        if self.map[pos[1]][pos[2]] <= 0:
            return None

        self.image.frame = self.map[pos[1]][pos[0]] - 1
        # if (pos[0]%5)==0:
        #     self.frame = 0
        # else:
        #     self.frame = 1
        ix = (pos[0]-pos[1])*22 + 400
        iy = (pos[0]+pos[1])*10 + 300
        self.image.pos = [ix, iy]
        return self.image

    def map_from_tpl(self):
        global map_tpl

        self.map = []
        for y in range(len(map_tpl)):
            row = map_tpl[y]
            rows = [[], [], [], []]
            for x in range(len(row)):
                w = row[x]
                for i in range(4):
                    for j in range(4):
                        rows[i].append(self.get_w(i, j, w))
            for i in range(4):
                self.map.append(rows[i])

    def get_w(self, i, j, w):
        if (i == 0)and(j == 0):
            return w*3
        elif (j <= 0):
            return w
        elif (i <= 0):
            return w*2
        elif (i == 3)and(j == 3):
            return w*6
        elif (j >= 3):
            return w*5
        elif (i >= 3):
            return w*4
        else:
            return 0
