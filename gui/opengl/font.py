#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  font.py
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
            
class Font():
    def __init__(self, family, size, bold=False ):
        import pygame, gui.opengl.texture
        
        self.render      = []
        self.screen_size = pygame.display.get_surface().get_size()
      
        font = pygame.font.SysFont(family, size, bold=bold)
        for i in range(ord(' '), ord('~')):
            game_char = font.render(chr(i), 1, (255,255,255))
            txt = gui.opengl.texture.Texture(game_char)
            self.render.append(txt)
        return
      
    def draw(self, text, x, y, **args):
      i=0   
      glPushMatrix()
      glLoadIdentity()
      glPushAttrib(GL_CURRENT_BIT) 
      glTranslatef(x, y + self.render[0].h/2, 0)
      if "color"  in args: glColor3f(*args['color'])
      if "scale"  in args: glScalef(args['scale'], args['scale'], 1.0)
      if "rotate" in args: glRotatef(-args['rotate'], 0, 0, 1)
      while i < len(text):
          ch = ord(text[i])-32
          glTranslatef(self.render[ch].w, 0, 0)
          glCallList(self.render[ch].newList)
          i += 1;
      glPopAttrib()           
      glPopMatrix()
      return
      
def main():
    return 0

if __name__ == '__main__':
    main()

