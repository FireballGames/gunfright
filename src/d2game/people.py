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
