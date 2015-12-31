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
""" Basic game module
"""


import d2game
import logging
import pygame


class UI(object):
    def win(self):
        logging.debug("Win game")

    def loose(self):
        logging.debug("Loose game")

    def stop(self):
        logging.debug("Stop game")

    def quit(self):
        logging.debug("Quit game")


class Game(object):

    def __init__(self, params):
        logging.info("Initialization game")

        import d2lib.reslib

        self.config = params
        self.resources = d2lib.reslib.Reslib()
        self.ui = None
        self.state = d2game.GAMEOVER
        self.subgames = []

        import gui

        # self.window    = sdl_window.SDLwindow(self.screen)
        gui.res = self.resources

        from .player import Player

        self.player = Player(params)

    def run(self):
        """When game starts"""
        logging.info("Running game")
        self.state = d2game.GAMEPLAY
        while self.state == d2game.GAMEPLAY:
            self.play()
            # self.draw_bg()
            # self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
            # self.draw_fg()
            # self.window.draw()

    def play(self):
        """Game main loop"""
        self.process_events()
        # self.window.clear()

    def play_subgame(self, index):
        if index not in range(len(self.subgames)):
            return False

        self.subgames[index].run()
        self.state = self.subgames[index].state
        if self.state == d2game.GAMELOOSE:
            self.loose()
        if self.state == d2game.GAMEWIN:
            self.state = d2game.GAMEPLAY
        print("--------------------")

        return True

    def process_events(self):
        """Processs game events"""
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                print("QUIT")
                self.loose()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                print("ESCAPE")
                self.loose()
            self.process_event(e)

    def process_event(self, event):
        """Process event"""
        pass

    def win(self):
        """When player wins the game"""
        logging.info('Player win')
        self.state = d2game.GAMEWIN
        if self.ui is not None:
            self.ui.win()

    def loose(self):
        """When player looses the game"""
        logging.info('Player loose')
        self.state = d2game.GAMELOOSE
        if self.ui is not None:
            self.ui.loose()

    def end(self):
        """When player stops the game"""
        logging.info('Player stops')
        if self.ui is not None:
            self.ui.stop()
        self.loose()

    def quit(self):
        """When player quits from the game"""
        logging.info('Player quits')
        if self.ui is not None:
            self.ui.quit()
        import sys

        sys.exit(0)


def main():
    return 0

if __name__ == '__main__':
    main()
