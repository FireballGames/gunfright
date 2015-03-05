#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sdlgui.py
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

import gui.screen, gui.pointer

i     = None
g     = None
gg    = None
mygui = None
screen_data = {}

class MainGui(gui.screen.Screen):
    pointer = False
    
    def __init__(self, **config):
        gui.screen.Screen.__init__(self, **config)
        self.image.set_colorkey([255, 0, 255])
        
        global g
        self.pointer = gui.pointer.Pointer(g.player)
            
    def blit_screen(self, window):
        global g
        
        import pygame, d2lib.config
        text = pygame.font.Font(None, d2lib.config.config()['text_size'])
        window.blit(text.render("Money "+str(g.player.score),    True, (255,0,0)), (500, 450))
        window.blit(text.render("Level "+str(g.level.score),     True, (255,0,0)), (500, 475))
        window.blit(text.render("Time  "+str(g.level.seconds()), True, (255,0,0)), (500, 500))
        pygame.draw.circle(window, (255, 255, 255), (226, 487), 65)
        window.blit(text.render(str(g.player.shots),             True, (255,0,0)), (200, 475))
        
        if(self.pointer):
            window.blit(*self.pointer.move())
    
def win():
    global mygui, screen_data
    
    s = screen.Screen(**screen_data['win'])
    s.show_screen(mygui.surface)

def loose():
    global mygui, screen_data
    
    s = gui.screen.Screen(**screen_data['loose'])
    s.show_screen(mygui.surface)

def main():
    return 0

if __name__ == '__main__':
    main()

