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
import gui
import gui.controls
import gunfright.player
import gunfright.subgame.bountyshooter
import gunfright.subgame.seekbandit


class Game(d2game.game.Game):

    def __init__(self, params):
        d2game.game.Game.__init__(self, params)

        self.player = gunfright.player.Player(self.config)

        gui.init_gui(self.config)
        gui.controls.Splash(self.config.screen('intro')).show()
        gui.init_game(self)

        self.subgames = [
            gunfright.subgame.bountyshooter.Game(self.player, self.config),
            gunfright.subgame.seekbandit.Game(self.player, self.config),
            gunfright.subgame.bountyshooter.Game(self.player, self.config)
        ]

    def win(self):
        d2game.game.Game.win(self)
        gui.win()

    def loose(self):
        d2game.game.Game.loose(self)
        gui.loose()
        self.quit()

    def play(self):
        d2game.game.Game.play(self)

        print("Running the game")
        print("Next level screen")
        screen = gui.controls.Splash(self.config.screen('nextlev'))
        screen.controls["text"] = gui.controls.ControlText(
            "Level %s",
            pos = (100, 100),
            size = 32,
        )
        screen.controls["text"].prepare(self.player.level)
        screen.show()
        print("--------------------")

        for i in range(len(self.subgames)):
            self.subgames[i].load_level(self.player.level)
            self.play_subgame(i)
            if self.state != d2game.GAMEPLAY:
                return
            print("--------------------")

        # print("Shoot bandit subgame")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        # if self.state != d2game.GAMEPLAY:
        #    return
        # print "--------------------"

        self.win()
        self.player.levelup()
        self.state = d2game.GAMEPLAY

        print("State: %s" % (self.state))
        print "--------------------"


def main():
    print("Gunfright game globals")
    return 0

if __name__ == '__main__':
    main()
