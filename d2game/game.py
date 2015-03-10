#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.py
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


from . import *

class Game(object):

    def __init__(self, params):
        print("Initialization game")
        self.config = params
        self.state = GAMEOVER

        import d2lib.reslib
        self.resources = d2lib.reslib.Reslib()

        import player
        self.player = player.Player(params)

    def play(self):
        """When game starts"""
        print("Playing game")
        self.state = GAMEPLAY

    def win(self):
        """When player wins the game"""
        print('You win')
        self.state = GAMEWIN

    def loose(self):
        """When player looses the game"""
        print('You loose')
        self.state = GAMELOOSE

    def end(self):
        """When player stops the game"""
        print('Player stop')
        self.loose()

    def quit(self):
        """When player quits from the game"""
        import sys

        sys.exit(0)


def main():
    print("Basic game module")
    return 0

if __name__ == '__main__':
    main()
