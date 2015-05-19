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

import pygame
import config


class Reslib():
    def __init__(self):
        pygame.font.init()

        self.images = {}

        c = config.config()
        for key in c.backgrounds.keys():
            self.images[key] = pygame.image.load(c.backgrounds[key])
        for key in c.controls.keys():
            self.images[key] = pygame.image.load(c.controls[key])

        self.images['icon'] = pygame.image.load(c.window["icon"])
        # self.images['intro'] = pygame.image.load("res/intro.png")

        self.font = pygame.font.Font(None, c.text_size)

    def args(self):
        return self.images.keys()

    def add_args(self, args):
        print("Args: %s" % (args))

    def load(self, index, alpha = False):
        image = self.images[index]
        if alpha:
            image.convert_alpha()
        return image

    def text(self):
        return self.font


def main():
    print("Resource library class")

if __name__ == '__main__':
    main()
