#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  texture.py
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

from OpenGL.GL import *
import pygame

class Texture():
    def __init__(self, src, pos=None):
        if isinstance(src, pygame.Surface):
            image = src
        else:
            image = pygame.image.load(src)
        
        # Resize texture from surface
        self.rect = image.get_rect()
        # ---
        self.w  = image.get_width()
        self.h  = image.get_height() 
        maxSize = glGetIntegerv(GL_MAX_TEXTURE_SIZE)
        surface = self.resize(image, maxSize)
        new_h   = image.get_height()
        new_w   = image.get_width()
        dw      = self.w/float(new_w)
        dh      = self.h/float(new_h)

        # if self.rect.w < 64: self.rect.w = 64;
        # if self.rect.h < 64: self.rect.h = 64;
        
        if not (pos is None): 
            self.pos = pos
        else:
            self.pos = [self.w/2, self.h/2, 0]

        texdata = pygame.image.tostring(image, "RGBA", 0)
        
        # OpenGL texture generation
        self.texture_id = glGenTextures(1)
        glBindTexture(  GL_TEXTURE_2D, self.texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(   GL_TEXTURE_2D, 0, GL_RGBA, new_w, new_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, texdata)

        # Making primitive for texture
        self.newList = glGenLists(1)
        glNewList(self.newList, GL_COMPILE)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(    0,     0, 0)
        glTexCoord2f(0, 1); glVertex3f(    0, new_h, 0)
        glTexCoord2f(1, 1); glVertex3f(new_w, new_h, 0)
        glTexCoord2f(1, 0); glVertex3f(new_w,     0, 0)
        glEnd()
        glEndList()
        
    def size_needed (self, texSize, current_size):
        import math
        
        newsize = pow(2, math.ceil(math.log(current_size)/math.log(2.0)))
        if(newsize > texSize): newsize = texSize
        return newsize

    def resize (self, image, texSize ):
        h1 = image.get_height()
        w1 = image.get_width()
        h2 = self.size_needed(texSize, h1)
        w2 = self.size_needed(texSize, w1)
        if ( h1 != h2 ) or ( w1 != w2 ):
            dst_rect = pygame.Rect(0,0,w2,h2)
            dest     = pygame.Surface((w2,h2), 0, image)
            dest.blit(image, (0,0), dst_rect)
            return dest
        else:
            return image  
            
    def draw(self, pos = (0, 0, 0), rotate = (0, 0, 0, 1), scale = 1.0):
        glPushAttrib(GL_TRANSFORM_BIT)
        glLoadIdentity()
        glRotatef(*rotate)
        glScalef(scale, scale, 1.0)
        glTranslatef(pos[0]-self.pos[0]*scale, pos[1]-self.pos[1]*scale, pos[2]-self.pos[2]*scale)
        glPopAttrib()
        glCallList(self.newList)

def main():
    return 

if __name__ == '__main__':
    main()

