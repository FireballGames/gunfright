#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  controls.py
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


import logging


class Splash():
    def __init__(self, config):
        import gui

        self.controls = {}
        self.sleep = 2
        self.bg_pos = (0, 0)

        if "background" in config:
            self.image = gui.res.load(config["background"])

        if "sleep" in config:
            self.sleep = config["sleep"]
        if "pos" in config:
            self.bg_pos = config["pos"]
        if "sound" in config:
            self.sound = config["sound"]

        self.rect = self.image.get_rect()
        self.rect.x += self.bg_pos[0] + (gui.gui.screen_size[0] - self.rect.width) / 2
        self.rect.y += self.bg_pos[1] + (gui.gui.screen_size[1] - self.rect.height) / 2

    def show(self):
        import gui
        import pygame
        import time

        # self.play_sound()
        # for e in pygame.event.get():
        #    self.process_event(e)

        gui.gui.surface.blit(self.image, self.rect)

        # self.blit_screen(window)
        for c in self.controls:
            self.controls[c].show(gui.gui.surface)

        pygame.display.update()

        if self.sleep:
            time.sleep(self.sleep)


class GUI():
    def __init__(self, config):
        import gui

        self.controls = {}

        if "background" in config:
            self.image = gui.res.load(config["background"])

        self.rect = self.image.get_rect()
        self.rect.x += (gui.gui.screen_size[0] - self.rect.width) / 2
        self.rect.y += (gui.gui.screen_size[1] - self.rect.height) / 2

    def show(self):
        import gui

        gui.gui.surface.blit(self.image, self.rect)

        for c in self.controls:
            self.controls[c].show(gui.gui.surface)


class MapPlayer():
    def __init__(self, config):
        import gui
        import pygame

        self.image = None

        if "image" in config:
            self.image = gui.res.load(config["image"])
        if "pos" in config:
            self.pos = [2, 2]
            # config["pos"]
        else:
            self.pos = [0, 0]

        self.tiles = [gui.res.load("grass"), gui.res.load("ground")]
        self.tile_rect = pygame.Rect((0, 0), (10, 10))

        if "map" in config:
            self.map = config["map"]
            self.map_array = self.map.map_array
        else:
            map_tpl = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
            self.map_array = []
            for row in map_tpl:
                map_row = []
                for p in row:
                    for scol in range(4):
                        map_row.append(p)
                for srow in range(4):
                    self.map_array.append(map_row)

        self.rect = self.image.get_rect()
        self.rect.x += self.pos[0] - (self.rect.width / 2)
        self.rect.y += self.pos[1] - (self.rect.height / 2)

    def tile_pos(self, *pos):
        rect_size = (64, 32)
        pos0 = (400 - rect_size[0], 0)
        return (
            ((pos[0] - pos[1]) * rect_size[0]) + pos0[0],
            ((pos[0] + pos[1]) * rect_size[1]) + pos0[1]
        )

    def show(self):
        import gui
        import pygame

        pos0 = (4, 4)
        player_pos0 = (4, 4)
        tile_size = (64, 32)
        player_size = (32, 0)
        y = 0
        for row in self.map_array:
            x = 0
            for p in row:
                t_r = pygame.Rect(self.tile_pos(
                        x - self.pos[0] + pos0[0],
                        y - self.pos[1] + pos0[1]
                    ),
                    tile_size
                )
                t = p.tile
                if self.tiles[t] is not None:
                    gui.gui.surface.blit(self.tiles[t], t_r)
                x += 1
            y += 1

        pos = self.tile_pos(*player_pos0)  # (2, 2)
        self.rect.x = pos[0] + (tile_size[0] + player_size[0]) / 2
        self.rect.y = pos[1] + (tile_size[1] + player_size[1]) / 2
        gui.gui.surface.blit(self.image, self.rect)


class ControlShoot():
    def __init__(self, pos = (0, 0), size = (0, 0)):
        self.pos = pos
        self.size = size

    def show(self):
        s = {
            'pos':  self.pos,
            'size': self.size
        }
        print(s)


class ControlImageList():
    def __init__(self, image, pos=[]):
        self.image = image
        self.pos = pos

    def show(self, count):
        for index in range(count):
            if index in range(len(self.pos)):
                self.image.show(self.pos[index])
            else:
                break


class ControlImage():
    def __init__(self, image):
        self.image = image

    def show(self, pos = (0, 0)):
        i = {
            'pos':   pos,
            'image': self.image,
        }
        print(i)


class ControlText():
    def __init__(self, template, pos = (0, 0), size = 8):
        self.template = template
        self.pos = pos
        self.size = size
        self.family = None
        self.color = (255, 255, 255)
        self.text = ""

        import pygame
        self.font = pygame.font.Font(self.family, self.size)

    def prepare(self, *vars):
        self.text = self.template % vars

    def show(self, window, text = "No text"):

        window.blit(self.font.render(self.text, True, self.color), self.pos)
        t = {
            'text': self.text,
            'pos': self.pos,
            'size': self.size,
        }
        print(t)


def main():
    return 0

if __name__ == '__main__':
    main()
