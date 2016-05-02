#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  seekbandit.py
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
""" Seekbandit subgaME
"""


import logging

import d2game.game
import d2game.map


class Game(d2game.game.Game):

    def __init__(self, player, params):
        d2game.game.Game.__init__(self, params)

        logging.info("Seek bandit subgame")

        self.player = player
        self.map = d2game.map.Map((16, 16))
        logging.debug(self.player.pos)

        import gui
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
                pos = (0, 0),
                size = 16
            ),
            'map': gui.controls.ControlText(
                '(%s)',
                pos = (400, 0),
                size = 16
            ),
            'player': gui.controls.MapPlayer({
                "pos": [400, 300],
                "image": "player",
                "map": self.map,
            })
        }
        self.screen = None
        self.gui = gui.res.load("gui")

    def run(self):
        logging.debug("Running bandit seeker")

        import gui
        gui.g = self

        self.load_level(self.player.level)
        d2game.game.Game.run(self)

    def play(self):
        import gui
        gui.gui.clear()

        d2game.game.Game.play(self)

        bandit = None
        if self.player.seek(bandit):
            self.win()
            return

        self.draw()

        import pygame
        pygame.display.flip()
        pygame.time.delay(2)

    def load_level(self, level):
        import config
        # import gunfright.level
        level_data = config.level(level)

        self.map.generate_map((16, 16))
        self.player.pos = [len(self.map.map_array)/2 - 2, len(self.map.map_array[0])/2 + 2]
        # global people, bandit
        # bandit = People(random.randrange(size_x*5), random.randrange(size_y*5))

    def move_objects(self):
        # global people, bandit
        # for p in people:
        #    # p.move(random.randrange(4))
        #    # if (p.pos[0]==player.pos[0])and(p.pos[1]==player.pos[1]):
        #        # print 'Hit by people'
        #        # return player.loose()
        #    # print p.pos
        # bandit.move(random.randrange(4))
        pass

    def draw_map(self):
        # draw_map(player.pos[0], player.pos[1], 8, 8)
        for i in range(len(self.map.map)):
            row = self.map.map[i]
            for j in range(len(row)):
                pass
                # im = self.map.draw((i, j))
                # if im is not None:
                #     self.window.draw_image(im)
        pass

    def draw(self):
        # self.draw_map()
        self.controls['player'].pos = self.player.pos
        self.controls['player'].show()

    def draw_controls(self):
        logging.debug({
            'player': self.player.pos,
            'score':  self.player.score,
            'shots':  self.player.shots,
            'lives':  self.player.lives
        })
        return

    def move_and_draw(self, direction):
        self.player.move(direction, self.map)
        self.draw_controls()

    def process_events(self):
        d2game.game.Game.process_events(self)

        import pygame

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_and_draw(d2game.map.DIR_UP)
        if keys[pygame.K_DOWN]:
            self.move_and_draw(d2game.map.DIR_DOWN)
        if keys[pygame.K_LEFT]:
            self.move_and_draw(d2game.map.DIR_LEFT)
        if keys[pygame.K_RIGHT]:
            self.move_and_draw(d2game.map.DIR_RIGHT)


def main():
    return 0

if __name__ == '__main__':
    main()
