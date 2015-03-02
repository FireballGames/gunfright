#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pointer.py
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

class Pointer(pygame.sprite.Sprite):
    def __init__(self, player, active = False):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("res/mouse.png")
        self.image.set_colorkey([255, 0, 255])
        self.rect   = self.image.get_rect()
        self.rect.x = 800/2
        self.rect.y = 600/2
        self.player = player
        self.active = active
        
    def move(self):
        position    = pygame.mouse.get_pos() 
        self.rect.x = position[0] 
        self.rect.y = position[1]
        return [self.image, self.rect]
    
    def in_active(self):
        if not self.active:
            return true
            
        return pygame.sprite.spritecollide(self, [self.active], dokill=False)
        
    def intersect(self, sprites, player):
        result = pygame.sprite.spritecollide(self, sprites, dokill=True)
        if result:
            import sound
            for sprite in result:
                player.score += 100
                sound.play_hit()
    
    def process_event(self, e, moneybags):
        import pygame, sound
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if self.in_active() and self.player.shoot():
                sound.play('res/sounds/shot.mp3')
                self.intersect(moneybags, self.player)
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 3:
            print "Right"
            self.player.reload()

def main():
    return 0

if __name__ == '__main__':
    main()

