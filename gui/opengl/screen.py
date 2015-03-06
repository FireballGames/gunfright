#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  screen.py
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
import gui.screen

class Screen(gui.screen.Screen):    
    def __init__(self, scene):
        # Clearing screen objects
        self.tiles    = []
        self.textures = []
        self.gui      = []
        
        self.mouse_tile = None
        
        gui.screen.Screen.__init__(self, scene)
            
        if not(self.background is None):
            bg_tile     = self.create_tile(self.create_texture(self.background))
            bg_tile.pos = self.scene.get_bg_pos()
            
        if not(self.mouse is None):
            self.set_mouse(self.mouse)

        # glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glPushMatrix()
        glOrtho(*self.scene.get_viewbox())
        glPopMatrix()
        
    def clear_window(self):
        glClearColor(*self.color)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    def draw(self):
        self.clear_window()
                    
        self.process_events()
        
        for t in self.tiles:
            t.draw()
        
        self.scene.draw()

        for g in self.gui:
            g.draw()

        if not(self.mouse_tile is None): self.mouse_tile.draw()
           
    # Working with tile
    def create_tile(self, src):
        import texture,tile
        if isinstance(src, texture.Texture):
            tex = src
        else:
            tex = texture.Texture(src)

        t     = tile.Tile(tex)
        t.pos = [0, 0, 0]
        self.tiles.append(t)
        return t

    # Working with tiles
    def create_texture(self, src):
        import pygame, texture
        
        t = texture.Texture(src)
        
        self.textures.append(t) 
        return t
        
    def create_font(self, family, size, bold=False):
        import gui.opengl.font
        f = gui.opengl.font.Font(family, size, bold)
        self.fonts.append(f)
        return f
        
    def create_gui(self, src):
        import texture, tile
        
        print src
        
        if isinstance(src, texture.Texture):
            t = tile.Tile(src)
        else:
            t = tile.Tile(texture.Texture(src))

        t.pos = [0, 0, -300]
        self.gui.append(t)
        return t
        
    def set_mouse(self, mouse):
        if not mouse: return
        
        import tile, texture
        
        self.mouse_tile = self.create_gui(mouse)
        self.mouse_tile.texture.pos[0] = (800 + self.mouse_tile.texture.w)/2
        self.mouse_tile.texture.pos[1] = (600 + self.mouse_tile.texture.h)/2
        self.mouse_tile.pos = self.scene.pos
        
    def process_events(self):
        gui.screen.Screen.process_events(self)
        
        import pygame
        
        self.m_pos = pygame.mouse.get_pos()
        if not(self.mouse_tile is None):
            self.mouse_tile.pos[0] = self.m_pos[0]
            self.mouse_tile.pos[1] = self.m_pos[1]
        
def main():
    return 0

if __name__ == '__main__':
    main()

