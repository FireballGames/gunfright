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

import pygame, screen

window = 0
p      = 0
i      = 0
g      = 0
level  = 0

class MainGui(screen.Screen):
    def blit_screen(self, window):
        global g, level
        
        import pygame, config
        text = pygame.font.Font(None, config.params['text_size'])
        window.blit(text.render("Money "+str(g.player.score),  True, (255,0,0)), (500, 450))
        window.blit(text.render("Level "+str(level.score),     True, (255,0,0)), (500, 475))
        window.blit(text.render("Time  "+str(level.seconds()), True, (255,0,0)), (500, 500))
        window.blit(text.render(str(g.player.shots),           True, (255,0,0)), (200, 475))

def init_win(config):
    global window
    
    window = pygame.display.set_mode(config['size'])
    pygame.display.set_caption(config['title'].encode("utf8"))
    icon = pygame.image.load(config['icon']).convert_alpha()       
    pygame.display.set_icon(icon)

def init_gui(config):
    pygame.init()
    init_win(config['window'])
    pygame.mouse.set_visible(False)

    import sound
    sound.init_sound(config['main_theme'])
    
def init_game(game):
    global p, i, g
    import pointer
    g = game
    p = pointer.Pointer(g.player)
    i = MainGui({
        'background': pygame.image.load("res/interface.png"),
        'bg_pos':     (0, 0),
        'sound':      False,
        'sleep':      False,
        'showing':    False,
        'interface':  False
    })
    
def win():
    global window
    
    s = screen.Screen({
        'background': pygame.image.load("res/win.png"),
        'bg_pos':     (0, 0),
        'sound':      False,
        'sleep':      2,
        'showing':    False,
        'interface':  False
    })
    s.show_screen(window)

def loose():
    global window
    
    s = screen.Screen({
        'background': pygame.image.load("res/loose.png"),
        'bg_pos':     (0, 0),
        'sound':      "loose",
        'sleep':      2,
        'showing':    False,
        'interface':  False
    })
    s.show_screen(window)

def main():
    return 0

if __name__ == '__main__':
    main()

