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

import pygame

class Screen(pygame.sprite.Sprite):
    bg_pos    = [0, 0]
    sleep     = False
    sound     = False
    showing   = False
    interface = False
    
    def __init__(self, **config):
        pygame.sprite.Sprite.__init__(self)
        if "background" in config:
            if isinstance(config["background"], pygame.Surface):
                self.image = config["background"]
            else:
                self.image = pygame.image.load(config["background"])
 
        if "sleep" in config:
            self.sleep     = config["sleep"]
        if "pos" in config:
            self.bg_pos    = config["pos"]
        if "sound" in config:
            self.sound     = config["sound"]
        if "showing" in config:
            self.showing   = config["showing"]
        if "interface" in config:
            self.interface = config["interface"]
            
        self.rect    = self.image.get_rect()
        print self.bg_pos
        self.rect.x += self.bg_pos[0]
        self.rect.y += self.bg_pos[1]
        print self.rect
 
    def blit_screen(self, window):
        pass
                
    def process_event(self, e):
        pass
        
    def play_sound(self):
        if self.sound:
            import sound
            sound.play(self.sound)

    def show_image(self, window):
        window.blit(self.image, self.rect)
        if(self.interface):
            self.interface.show_image(window)
        self.blit_screen(window)

    def show_screen(self, window):
        self.play_sound()
        
        for e in pygame.event.get():
            self.process_event(e)

        self.show_image(window)
        pygame.display.update()

        if self.sleep:
            import time
            time.sleep(self.sleep)
                        
class PlayScreen(Screen):
    showing = False
    
    def __init__(self, **config):
        Screen.__init__(self, **config)

        if "showing" in config:
            self.showing     = config["showing"]

    def show_screen(self, window):
        self.play_sound()
        
        while self.showing:
            for e in pygame.event.get():
                self.process_event(e)
            self.show_image(window)
            pygame.display.flip()
            pygame.time.delay(self.sleep)
            # 10
            
def main():
    return 0

if __name__ == '__main__':
    main()

