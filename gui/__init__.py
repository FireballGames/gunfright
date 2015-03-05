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

class FpsCounter():
    t       = 0
    t_start = 0
    fps     = 0
    frames  = 0
    
    def get_fps(self):
        self.t       = pygame.time.get_ticks()
        self.frames += 1
        
        dt = (self.t - self.t_start)
        if dt > 1000:
            self.fps     = self.frames * 1000 / dt
            self.t_start = self.t
            self.frames  = 0
            
        return self.fps

class PygameWin():
    gamestate   = True
    main_theme  = False
    screen_size = [800, 600]
    screens     = []
    fonts       = []
    screen      = None
    
    def __init__(self, **args):
        pygame.init()
        self.fps = FpsCounter()

        # screen_data = config['screens']

        self.init_window(**args)
        
        if 'main_theme' in args: self.main_theme = args['main_theme']
        
        if self.main_theme:
            import sound
            sound.init_sound(self.main_theme)

    def init_window(self, **args):
        """Init SDL window"""
        flag        = pygame.DOUBLEBUF
        show_mouse  = False
        title       = 'New game'
        icon        = None
        
        if 'size'       in args: self.screen_size = args['size']
        if 'flag'       in args: flag             = args['flag']
        if 'title'      in args: title            = args['title']
        if 'icon'       in args: icon             = args['icon']
        if 'show_mouse' in args: show_mouse       = args['show_mouse']
        
        self.surface = pygame.display.set_mode(self.screen_size, flag)
        
        pygame.display.set_caption(title.encode("utf8"))

        if icon:
            icon_image = pygame.image.load(icon).convert_alpha()       
            pygame.display.set_icon(icon_image)

        pygame.mouse.set_visible(show_mouse)
        
    def clear_window(self):
        pygame.display.flip()
        
    def game_exit(self):
        """Stop game and exit to system"""
        import sys
        sys.exit()
        
    def process_events(self):
        import gui.screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gamestate = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.gamestate = False
               
            if isinstance(self.screen, gui.screen.Screen): 
                if event.type == self.screen.scene.LIFETIME:
                    self.screen.scene.gamestate = False
        
    def draw(self, *args):
        if not (self.screen is None): self.screen.draw()
        
        if len(self.fonts) > 0:
            output_data = "FPS %s"%(self.fps.get_fps())
            self.fonts[0].draw(output_data, -self.screen_size[0]/2,  -self.screen_size[1]/2, color=(1,1,1)) 
            # scale=0.2,
            
        for e in args:
            e.draw()
        
    def repaint(self, *args):
        """Game main loop"""
        self.process_events()
        self.draw(*args)
        pygame.display.flip()
            
    def release_screens(self, screen):
        self.screens = [screen]
        self.screen  = screen

def main():
    return 0

if __name__ == '__main__':
    main()

