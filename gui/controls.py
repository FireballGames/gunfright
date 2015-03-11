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
        self.rect.x += self.bg_pos[0]
        self.rect.y += self.bg_pos[1]

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


class ControlShoot():
    def __init__(self, pos = (0, 0), size = (0, 0)):
        self.pos = pos
        self.size = size

    def show(self):
        s = {
            'pos':  self.pos,
            'size': self.size
        }
        print s


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
        print i


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
        print t


def main():
    return 0

if __name__ == '__main__':
    main()
