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
""" Gunfright game globals
"""

import d2game.game
import logging

import gui
import gui.controls

class d2UI(d2game.game.UI):
    def __init__(self, game, config):
        self.game = game
        self.config = config

        gui.init_gui(self.config)
        gui.controls.Splash(self.config.screen('intro')).show()
        gui.init_game(self.game)

    def win(self):
        gui.win()

    def loose(self):
        gui.loose()
        self.game.quit()

    def next_level(self):
        screen = gui.controls.Splash(self.config.screen('nextlev'))
        screen.controls["text"] = gui.controls.ControlText(
            "Level %s",
            pos = (100, 100),
            size = 32,
        )
        screen.controls["text"].prepare(self.game.player.level)
        screen.show()


import gunfright.player
import gunfright.subgame.bountyshooter
import gunfright.subgame.seekbandit

class Game(d2game.game.Game):

    def __init__(self, params):
        d2game.game.Game.__init__(self, params)

        self.player = gunfright.player.Player(self.config)
        self.ui = d2UI(self, self.config)

        self.subgames = [
            # gunfright.subgame.bountyshooter.Game(self.player, self.config),
            gunfright.subgame.seekbandit.Game(self.player, self.config),
            gunfright.subgame.bountyshooter.Game(self.player, self.config)
        ]

    def win(self):
        d2game.game.Game.win(self)
        self.player.levelup()
        self.state = d2game.GAMEPLAY

    def play(self):
        d2game.game.Game.play(self)

        logging.info("Running the game")

        self.next_level()
        for i in range(len(self.subgames)):
            self.subgames[i].load_level(self.player.level)
            self.play_subgame(i)
            if self.state != d2game.GAMEPLAY:
                return
            logging.debug("Next subgame")
        self.shoot_bandit()
        self.win()

        logging.debug("State: %s" % (self.state))
        logging.debug("--------------------")

    def next_level(self):
        logging.debug("Next level screen")
        self.ui.next_level()

    def shoot_bandit(self):
        logging.debug("Shoot bandit subgame")
        # self.player.bonus = True
        # self.subgames[2].load_level(self.player.level)
        # self.play_subgame(2)
        if self.state != d2game.GAMEPLAY:
           return


def main():
    return 0

if __name__ == '__main__':
    main()
