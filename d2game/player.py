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


class Player():

    def __init__(self, config):
        if config.player:
            self.player.config.update(config.player)

        self.score = 0
        self.level = 1
        self.lives = 3
        self.pos   = [0, 0]
        self.dir   = 0

    def levelup(self):
        self.level += 1


def main():
    return 0

if __name__ == '__main__':
    main()
