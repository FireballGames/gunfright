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

map_tpl = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1],
    [1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,1],
    [1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map():
    def __init__(self):
        global map_tpl
        
        self.map = []
        for y in range(len(map_tpl)):
            row  = map_tpl[y]
            rows = [[],[],[],[]]
            for x in range(len(row)):
                w = row[x]
                for i in range(4):
                    for j in range(4):
                        if (i==0)and(j==0):
                            rows[i].append(w*3)
                        elif (j<=0):
                            rows[i].append(w)
                        elif (i<=0):
                            rows[i].append(w*2)
                        elif (i==3)and(j==3):
                            rows[i].append(w*6)
                        elif (j>=3):
                            rows[i].append(w*5)
                        elif (i>=3):
                            rows[i].append(w*4)
                        else:
                            rows[i].append(0)
            for i in range(4):
                self.map.append(rows[i])
        
        import sdl_sprite
        self.image = sdl_sprite.SDLSprite('res/border.png', (24, 24))
    def draw(self, pos):
        if self.map[pos[1]][pos[0]] > 0:
            self.image.frame = self.map[pos[1]][pos[0]] - 1
            # if (pos[0]%5)==0:
            #     self.frame = 0
            # else:
            #     self.frame = 1
            ix = (pos[0]-pos[1])*22 + 400
            iy = (pos[0]+pos[1])*10 + 300
            self.image.pos = [ix, iy]
            return self.image
        
class MyPlayer(game.Player):
    def __init__(self):
        game.Player.__init__(self)
        
        import sdl_sprite
        
        self.images     = sdl_sprite.SDLSprite('res/quickdraw.png', (21, 35))
        self.images.pos = [50, 30] 

        self.speed = 1.2

class MyGame(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        
        import sdl_sprite
        
        self.d2image1     = sdl_sprite.SDLSprite('res/money.png')
        self.d2image1.pos = ( 10, 20)
        self.d2image2     = sdl_sprite.SDLSprite('res/money.png')
        self.d2image2.pos = (220, 20)
        self.player       = MyPlayer()
        self.map = Map()
        # self.player.collisions = [self.d2image2]
        
    def process_events(self):
        game.Game.process_events(self)
        
        import pygame
        
        keys = pygame.key.get_pressed()
        if   keys[pygame.K_UP]:    self.player.move(  0, -1)
        elif keys[pygame.K_DOWN]:  self.player.move(  0,  1)
        elif keys[pygame.K_LEFT]:  self.player.move( -1,  0)
        elif keys[pygame.K_RIGHT]: self.player.move(  1,  0)
        
    def draw_bg(self):
        game.Game.draw_bg(self)
        for i in range(len(self.map.map)):
            row = self.map.map[i]
            for j in range(len(row)):
                im = self.map.draw((i, j))
                if not im is None:
                    self.window.draw_image(im)
        self.window.draw_image(self.d2image1)        

    def draw_fg(self):
        game.Game.draw_fg(self)
        self.window.draw_image(self.d2image2)        

def main():
    game = MyGame()
    game.play()
    return 0

if __name__ == '__main__':
	main()

