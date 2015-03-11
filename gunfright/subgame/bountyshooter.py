#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bountyshooter.py
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
import gui.controls


class Game(d2game.game.Game):

    def __init__(self, player, params):
        d2game.game.Game.__init__(self, params)
        self.player = player
        self.state = d2game.GAMEPLAY
        self.load_level(self.player.level)
        self.controls = {
            'main': gui.controls.ControlShoot(
                pos = (1, 1),
                size = (100, 100)
            ),
            'shots': gui.controls.ControlImageList(
                gui.controls.ControlImage('Revolver'),
                pos = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6))
            ),
            'lives': gui.controls.ControlImageList(
                gui.controls.ControlImage('Hat'),
                pos = ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1))
            ),
            'score': gui.controls.ControlText(
                '$%s',
                pos=(0, 0),
                size=16
            )
        }

    def run(self):
        print("Shoot money subgame")
        if not self.player.bonus:
            return

        print("Running bounty shooter")
        # d2game.game.Game.play(self)

        import screens.shootmoney
        screens.shootmoney.show(self)

    def load_level(self, level):
        import config
        import gunfright.level
        level_data = config.level(level)

        if level_data['type'] == 'bounty':
            level_data['player'] = self.player
            self.level = gunfright.level.ShootBounty(**level_data)

    def draw(self):
        self.controls['main'].show()
        self.controls['shots'].show(self.player.shots)
        self.controls['lives'].show(self.player.lives)
        self.controls['score'].show(self.player.score)


def main():
    print("Gunfright game globals")
    return 0

if __name__ == '__main__':
    main()
