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
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image     = config["background"]
        self.sleep     = config["sleep"]
        self.bg_pos    = config["bg_pos"]
        self.sound     = config["sound"]
        self.showing   = config["showing"]
        self.interface = config["interface"]
        print config

    def blit_screen(self, window):
        pass
                
    def process_event(self, e):
        pass
                
    def show_image(self, window):
        if(self.interface):
            self.interface.show_image(window)
        window.blit(self.image, self.bg_pos)
        self.blit_screen(window)

    def show_screen(self, window):
        if self.sound:
            import sound
            sound.play(self.sound)
        
        while self.showing:
            for e in pygame.event.get():
                self.process_event(e)
            self.show_image(window)
            pygame.display.flip()
            pygame.time.delay(10)

        if self.sleep:
            self.show_image(window)
            pygame.display.update()

            import time
            time.sleep(self.sleep)
            
def main():
    return 0

if __name__ == '__main__':
    main()

