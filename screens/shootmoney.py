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

import pygame, random, gui

class Moneybag(pygame.sprite.Sprite):
    def __init__(self, level, config):
        pygame.sprite.Sprite.__init__(self)
        self.image  = level.moneybag

        self.timer = pygame.time.Clock()

        self.dir = level.dir()

        self.boxsize = config['boxsize']
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

class ShootMoney(gui.screen.Screen):
    
    def blit_screen(self, window):
        import gui
        global moneybags
        
        if gui.g.lost:
            self.showing = False
            return self.showing;

        if gui.level.finish():
            gui.g.end_lev()
            self.showing = False
            return self.showing;
        
        if gui.level.can_add_bag():
            rect = self.image.get_rect()
            moneybags.add(Moneybag(gui.level, {
                'boxsize': [rect.width, rect.height]
            }))
            
        import pygame, config
        for moneybag in moneybags:
            img = moneybag.move()
            if img:
                window.blit(*img)
        gui.window.blit(*gui.p.move())
        return self.showing         

    def init_win(self):
        import pygame, gui
        global moneybags
    
        gui.p.active = self
        moneybags = pygame.sprite.Group()
        
    def process_event(self, e):
        import gui
        if e.type == pygame.QUIT:
            self.showing = False
            gui.g.stop()
        
        gui.p.process_event(e, moneybags)
    
moneybags = 0

def show(game, newlevel):
    global moneybags
    
    import gui, pygame
    
    gui.level = newlevel
    gui.g     = game

    print "Showing shooter"
    screen = ShootMoney({
        'background': gui.level.background,
        'bg_pos':     (32, 32),
        'sound':      False,
        'sleep':      False,
        'showing':    True,
        'interface':  gui.i
    })
    screen.init_win()
    screen.show_screen(gui.window)
    gui.p.active = False

def main():
    show()
    return 0

if __name__ == '__main__':
    main()
