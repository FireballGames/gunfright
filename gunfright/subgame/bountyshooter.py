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


class Game(d2game.game.Game):

    def __init__(self, player, params):
        d2game.game.Game.__init__(self, params)
        self.player = player
        self.state = d2game.GAMEPLAY
        self.load_level(self.player.level)

    def run(self):
        print("Running bounty shooter")
        # d2game.game.Game.play(self)

        import screens.shootmoney
        screens.shootmoney.show(self)

    def load_level(self, level):
        import config
        import gunfright.level
        level_data = config.level(level)

        print level_data['type']
        if level_data['type'] == 'bounty':
            level_data['player'] = self.player
            self.level = gunfright.level.ShootBounty(**level_data)


def main():
    print("Gunfright game globals")
    return 0

if __name__ == '__main__':
    main()
