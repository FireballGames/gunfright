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

import pygame, sdl_window

class Game():
    def __init__(self):
        self.screen = {
            'size':  (800, 600),
            'flags': pygame.DOUBLEBUF
        }
        self.window    = sdl_window.SDLwindow(self.screen)
        self.gamestate = 1
    
    def stop(self):
        """Exit from game"""
        self.gamestate = 0
        # import sys
        # sys.exit(0)

    def process_events(self):
        """Processing game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: self.stop()        
    
    def play(self):
        """Game main loop"""
        while self.gamestate:
            self.process_events()
            self.window.draw()

def main():
    game = Game()
    game.play()
    return 0

if __name__ == '__main__':
    main()

