#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shootmoney.py
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

import pygame, random, pointer

class Moneybag(pygame.sprite.Sprite):
    def __init__(self, level):
        pygame.sprite.Sprite.__init__(self)
        self.image  = level.moneybag

        self.timer = pygame.time.Clock()

        self.dir = level.dir()

        self.boxsize = (800, 600)
        self.padding = 64
        self.start   = True
        self.ticks   = 0
        self.tpf     = 100

        self.rect   = self.image.get_rect()

    def move(self):
        if self.start:
            self.rect.x = random.randrange(self.padding, self.boxsize[0]-self.padding)
            self.rect.y = 0
            self.start  = False
            return [self.image, self.rect]
           
        self.ticks += self.timer.tick()
        if self.ticks >= self.tpf:
            self.ticks = 0
            self.rect.x += self.dir[0]
            self.rect.y += self.dir[1]  
            
        if (self.rect.x not in range(self.boxsize[0])) or (self.rect.y not in range(self.boxsize[1])):
            del self
            return False
        else:
            return [self.image, self.rect]

moneybags = 0
interface = 0

def init_win():
    import pygame
    global moneybags, interface
    
    moneybags = pygame.sprite.Group()
    interface = pygame.image.load("res/interface.png")

def show_screen(player, level):
    import gui
    global interface, moneybags
    
    gui.window.blit(interface,  (0, 0))
    gui.window.blit(level.background, (16, 16))
    
    import pygame, config
    text = pygame.font.Font(None, config.params['text_size'])
    gui.window.blit(text.render("Money "+str(player.score),    True, (255,0,0)), (500, 450))
    gui.window.blit(text.render("Level "+str(level.score),     True, (255,0,0)), (500, 475))
    gui.window.blit(text.render("Time  "+str(level.seconds()), True, (255,0,0)), (500, 500))
    for moneybag in moneybags:
        img = moneybag.move()
        if img:
            gui.window.blit(*img)
    gui.window.blit(*gui.p.move())
    pygame.display.flip()
    pygame.time.delay(10)         

def show(game, level):
    global moneybags
    
    import gui, pygame, sound
    
    init_win()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                game.stop()
            gui.p.process_event(e, moneybags)
        
        if game.lost:
            break;
        
        if level.finish():
            game.end_lev()
            break;

        if level.can_add_bag():
            moneybags.add(Moneybag(level))

        show_screen(game.player, level)

def main():
    show()
    return 0

if __name__ == '__main__':
    main()
