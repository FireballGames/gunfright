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


import d2game.game
import gunfright.player
import gunfright.subgame.bountyshooter
import gui


class Game(d2game.game.Game):

    def __init__(self, params):
        d2game.game.Game.__init__(self, params)
        self.player = gunfright.player.Player(self.config)

        import screens.intro

        gui.init_gui(self.config)
        screens.intro.show(self.config.screen('intro'))
        gui.init_game(self)

        self.subgames = [
            gunfright.subgame.bountyshooter.Game(self.player, self.config)
        ]
        self.state = d2game.GAMEPLAY

    def win(self):
        d2game.game.Game.win(self)
        gui.win()

    def loose(self):
        d2game.game.Game.loose(self)
        gui.loose()
        self.quit()

    def play(self):
        print("Running the game")
        d2game.game.Game.play(self)

        print("Next level screen")
        import screens.nextlev
        screens.nextlev.show(self)

        print("Shoot money subgame")
        self.subgames[0].load_level(self.player.level)
        self.play_subgame(0)

        print("Main subgame")

        print("Shoot bandit subgame")

        self.win()
        self.player.level += 1

        print("State: %s"%(self.state))

    def play_subgame(self, index):
        self.subgames[index].play()
        self.state = self.subgames[index].state
        if self.state == d2game.GAMELOOSE: self.loose()
        if self.state == d2game.GAMEWIN: self.win()

def main():
    print("Gunfright game globals")
    return 0

if __name__ == '__main__':
    main()
