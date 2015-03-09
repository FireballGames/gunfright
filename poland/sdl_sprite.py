#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sdl_sprite.py
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

class SDLSprite():
    def __init__(self, src, size=[0, 0]):
        image   = pygame.image.load(src)
        rect    = image.get_rect()
        
        if size[0] <= 0: size[0] = rect.width
        if size[1] <= 0: size[1] = rect.height        
        self.rect = pygame.Rect(0, 0, size[0], size[1])   

        self.images = []
        for i in range(rect.height / size[1]):
            self.rect.top = i*size[1]
            row = []
            for j in range(rect.width / size[0]):
                self.rect.left = j*size[0]
                row.append(image.subsurface(self.rect))
            self.images.append(row)
            
        self.row     = 0
        self.frame   = 0
        self.animate = False
        self.pos     = [0, 0]
        
    def __getitem__(self, index):
        return self.images[self.row][index]
        
    def draw(self):
        image_row = self.images[self.row]
        if self.animate:
            self.frame += 1
            if self.frame >= len(image_row): self.frame = 0
        return image_row[self.frame]
        
    def collision(self, pos, sprite):
        if int(pos[0]) in range(self.pos[0]-sprite.rect.width, self.pos[0] + self.rect.width) \
            and int(pos[1]) in range(self.pos[1]-sprite.rect.height, self.pos[1] + self.rect.height): return True 
        return False

def main():
    return 0

if __name__ == '__main__':
    main()

