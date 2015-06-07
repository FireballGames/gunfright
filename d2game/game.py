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


import d2game
import pygame


class Game(object):

    def __init__(self, params):
        print("Initialization game")
        self.config = params
        self.state = d2game.GAMEOVER
        self.subgames = []

        import gui
        # self.window    = sdl_window.SDLwindow(self.screen)

        import d2lib.reslib
        self.resources = d2lib.reslib.Reslib()
        gui.res = self.resources

        from .player import Player

        self.player = Player(params)

    def run(self):
        """When game starts"""
        print("Playing game")
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
        print('You win')
        self.state = d2game.GAMEWIN

    def loose(self):
        """When player looses the game"""
        print('You loose')
        self.state = d2game.GAMELOOSE

    def end(self):
        """When player stops the game"""
        print('Player stop')
        self.loose()

    def quit(self):
        """When player quits from the game"""
        import sys

        sys.exit(0)


def main():
    print("Basic game module")
    return 0

if __name__ == '__main__':
    main()
