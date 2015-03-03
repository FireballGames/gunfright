#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nextlev.py
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

import gui
g = 0

class NextLev(gui.screen.Screen):
    def blit_screen(self, window):
        global g
        
        import pygame, config
        text = pygame.font.Font(None, config.params['text_size'])
        window.blit(text.render("Level "+str(g.player.level), True, (255, 255, 255)), (400, 300))


def show(game):
    import pygame
    global g
    g = game
    
    print "Showing next level"
    import config
    screen = NextLev(**config.screen('nextlev'))
    screen.show_screen(gui.window)

def main():
    import game
    g = Game({})
    show(g)
    return 0

if __name__ == '__main__':
    main()
