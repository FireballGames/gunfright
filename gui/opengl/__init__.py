#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
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
import gui
        
class OpenGLWin(gui.PygameWin):
    def init_window(self, **args):
        gui.PygameWin.init_window(self, **args)
        
        screen_points = (
            (-self.screen_size[0]/2, -self.screen_size[1]/2, -self.screen_size[1]/2),
            ( self.screen_size[0]/2,  self.screen_size[1]/2,  self.screen_size[1]/2),
        )
        
        if 'background_color' in args: self.background_color = args['background_color']
        if 'view_box'         in args:
            self.view_box = args['view_box']
        else:
            self.view_box = (
                screen_points[0][0], screen_points[1][0],
                screen_points[1][1], screen_points[0][1],
                screen_points[0][2], screen_points[1][2],
            )
            
        print "Initalizing OpenGL..."
        print self.view_box

        # Set projection matrix
        # Load identity matrix
        # Set orthogonal screen range
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(*self.view_box)
        
        # Set model matrix
        glMatrixMode(GL_MODELVIEW)

        # Setting up OpenGL server for textures
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        self.create_font('CourierNew', 16, True)
        
        self.load_textures()
        
    def load_textures(self):
        pass
        
    # def process_events(self):
        # gui.PygameWin.process_events(self)
    
    # Working with screen
    def create_screen(self, scene):
        import gui.opengl.screen
        
        s = gui.opengl.screen.Screen(scene)
        s.gamestate = self.gamestate
        self.screens.append(s)
        
        if self.screen is None: self.screen = s
        return s
        
    def only_screen(self, scene):
        s = self.create_screen(scene)
        self.release_screens(s)
        return s
        
    def create_font(self, family, size, bold=False):
        import gui.opengl.font
        f = gui.opengl.font.Font(family, size)
        self.fonts.append(f)
        return f
        
    def show(self, *args):
        while True:
            self.repaint(*args)

            if not(self.screen is None):
                self.gamestate = self.screen.gamestate
                if not self.screen.scene.gamestate: return

            if not self.gamestate: return

def main():
    return 0

if __name__ == '__main__':
    main()

