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

class Player():
    def __init__(self):
        self.images  = None
        self.speed   = 1
        
        self.collisions = []
        
    def move(self, *coords):
        """Move player by coords"""
        self.images.animate = True
        newpos = [
            self.images.pos[0],
            self.images.pos[1]
        ]
        for i in range(len(coords)):
            newpos[i] += coords[i]*self.speed
        for c in self.collisions:
            if c.collision(newpos, self.images): return
        self.images.pos = newpos
                    
    def draw(self):
        # print self.images.animate
        image = self.images.draw()
        self.images.animate = False
        return image

class Game():
    def __init__(self):
        self.screen = {
            'size':  (800, 600),
            'flags': pygame.DOUBLEBUF
        }
        self.window    = sdl_window.SDLwindow(self.screen)
        self.gamestate = 1
        self.player    = None
    
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
    
    def draw_bg(self):
        self.window.clear()
        
    def draw_fg(self):
        pass
        
    def draw(self):
        """Game window drawing"""
        self.draw_bg()
        self.window.draw_image_pos(self.player.draw(), self.player.images.pos)
        self.draw_fg()
        self.window.draw()
    
    def play(self):
        """Game main loop"""
        while self.gamestate:
            self.process_events()
            self.draw()

def main():
    game = Game()
    game.play()
    return 0

if __name__ == '__main__':
    main()

