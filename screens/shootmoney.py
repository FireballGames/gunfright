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
    ticks = -1
    box   = 0
    
    def __init__(self, image, bounty, config):
        pygame.sprite.Sprite.__init__(self)
        
        if image:
            self.image = image
            self.rect  = self.image.get_rect()
        self.dir = bounty.dir
            
        self.timer = pygame.time.Clock()

        self.box = config['rect']
        self.tpf = config['tpf']
        
        print "Before"
        print self.box
        print self.rect
        self.box.x      -= self.rect.width
        self.box.y      -= self.rect.height
        self.box.width  += self.rect.width  * 2
        self.box.height += self.rect.height * 2
        print "After"
        print self.box

    def move(self):
        if self.ticks < 0:
            self.rect.x = self.box.x + random.randrange(self.box.width)
            self.rect.y = self.box.y
            self.ticks  = self.timer.tick()
            return [self.image, self.rect]
           
        self.ticks += self.timer.tick()
        if self.ticks >= self.tpf:
            self.ticks = 0
            self.rect.x += self.dir[0]
            self.rect.y += self.dir[1]
            
        if not self.box.contains(self.rect):
            del self
            return False
        else:
            return [self.image, self.rect]

class ShootMoney(gui.screen.PlayScreen):
    def blit_screen(self, window):
        import gui
        global moneybags
        
        if gui.g.lost:
            self.showing = False
            return self.showing;

        if gui.g.level.is_finished():
            gui.g.end_lev()
            self.showing = False
            return self.showing;
        
        b = gui.g.level.add_bounty() 
        if b:
            moneybags.add(Moneybag(self.moneybag, b, {
                'rect': self.rect.copy(),
                'tpf':  100
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

        self.moneybag    = pygame.image.load("res/money.png")
        self.moneybag.set_colorkey([255, 0, 255])

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
    import config
    level_config = config.screen('shootmoney')
    level_config.update({
        'background': gui.level.background,
        'pos':        (32, 32),
        'interface':  gui.i
    })
    screen = ShootMoney(**level_config)
    screen.init_win()
    screen.show_screen(gui.window)
    gui.p.active = False

def main():
    show()
    return 0

if __name__ == '__main__':
    main()
