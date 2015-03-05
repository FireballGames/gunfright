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

class Screen():
    
    def __init__(self, scene):
        self.scene        = scene
        self.scene.screen = self
        
        self.config = scene.config

        # Default values
        self.background = None
        self.mouse      = None
        self.sound      = False
        self.color      = (0.0, 0.0, 0.0, 1.0)
        
        self.fonts    = []

        # Load from config
        if "sound" in self.config: self.sound = self.config["sound"]
        if 'color' in self.config: self.color = self.config['color']
        
        if ("background" in self.config) and self.config['background']:
            if isinstance(self.config["background"], pygame.Surface):
                self.background = self.config["background"]
            else:
                self.background = pygame.image.load(self.config["background"])

        if ("mouse" in self.config) and self.config['mouse']:
            if isinstance(self.config["mouse"], pygame.Surface):
                self.mouse = self.config["mouse"]
            else:
                self.mouse = pygame.image.load(self.config["mouse"])


        if not (self.background is None):
            self.rect = self.background.get_rect()
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)

        bg_pos = self.scene.get_bg_pos()
        self.rect.x += bg_pos[0]
        self.rect.y += bg_pos[1]
        
        self.scene.init_controls(self)
         
    def blit_screen(self, window):
        pass
    
    def process_events(self):        
        keys = pygame.key.get_pressed()
        # Movement keys
        # if keys[pygame.K_SPACE]:
            # self.gamestate = False
        pass
        
    def play_sound(self):
        if self.sound:
            import sound
            sound.play(self.sound)

    def show_image(self, window):
        window.blit(self.image, self.rect)
        self.blit_screen(window)
        if(self.interface):
            self.interface.show_image(window)

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

