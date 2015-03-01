#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gui.py
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

window = 0
p      = 0

class Screen(pygame.sprite.Sprite):
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        # "res/intro.png"
        # 2
        # (0, 0)
        # intro
        self.image  = pygame.image.load(config["background"])
        self.sleep  = config["sleep"]
        self.bg_pos = config["bg_pos"]
        self.sound  = config["sound"]

    def blit_screen(self):
        pass
                
    def show_screen(self):
        global window
        
        if self.sound:
            import sound
            sound.play(self.sound)
        
        window.blit(self.image, self.bg_pos)
        self.blit_screen()
        
        pygame.display.update()
        if self.sleep:
            import time
            time.sleep(self.sleep)

def init_gui(config):
    global window
    
    pygame.init()
    window = pygame.display.set_mode(config['win_size'])
    pygame.display.set_caption(config['title'])
    icon = pygame.image.load(config['icon']).convert_alpha()       
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(False)

    import sound
    sound.init_sound()
    
def init_game(game):
    global p
    import pointer
    p = pointer.Pointer(game.player)
    
def win():
    global window
    
    import time
    background_w = pygame.image.load("res/win.png")
    window.blit(background_w, (0,0))
    pygame.display.update()
    time.sleep(2)

def loose():
    global window
    
    import pygame, sound, time
    background_l = pygame.image.load("res/loose.png")
    window.blit(background_l, [0,0])
    pygame.display.update()
    sound.play_loose()
    time.sleep(2)

def main():
    return 0

if __name__ == '__main__':
    main()

