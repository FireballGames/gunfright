#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run.py
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

import game


class MyPlayer(game.Player):
    def __init__(self):
        game.Player.__init__(self)

        import sdl_sprite

        self.images = sdl_sprite.SDLSprite('res/quickdraw.png', (21, 35))
        self.images.pos = [50, 30]

        self.speed = 1.2


class MyGame(game.Game):
    def __init__(self):
        game.Game.__init__(self)

        self.player = MyPlayer()
        # self.map = Map()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(0, -1)
        elif keys[pygame.K_DOWN]:
            self.player.move(0, 1)
        elif keys[pygame.K_LEFT]:
            self.player.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.player.move(1, 0)

    def draw_bg(self):
        game.Game.draw_bg(self)
        for i in range(len(self.map.map)):
            row = self.map.map[i]
            for j in range(len(row)):
                im = self.map.draw((i, j))
                if im is not None:
                    self.window.draw_image(im)
        self.window.draw_image(self.d2image1)

    def draw_fg(self):
        game.Game.draw_fg(self)
        self.window.draw_image(self.d2image2)


def main():
    game = MyGame()
    game.play()
    return 0
