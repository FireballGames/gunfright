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

i      = None
g      = None
gui    = None

screen_data = {}

class PygameWin():
    gamestate   = True
    main_theme  = False
    
    def __init__(self, **args):
        screen_size = [800, 600]
        flag        = pygame.DOUBLEBUF
        show_mouse  = False
        title       = 'New game'
        icon        = None
        
        pygame.init()


        # screen_data = config['screens']
        if 'screen_size' in args:
            screen_size = args['screen_size']
        if 'flag' in args:
            flag = args['flag']

        self.surface = pygame.display.set_mode(screen_size, flag)

        if 'title' in args:
            title = args['title']
        if 'icon' in args:
            icon = pygame.image.load(args['icon']).convert_alpha()       
        if 'show_mouse' in args:
            show_mouse = args['show_mouse']

        pygame.display.set_caption(title.encode("utf8"))
        if icon:
            pygame.display.set_icon(icon)
        pygame.mouse.set_visible(show_mouse)
        
        if 'main_theme' in args:
            self.main_theme = args['main_theme']
        
        if self.main_theme:
            import sound
            sound.init_sound(self.main_theme)
 
    def game_exit(self):
        """Stop game and exit to system"""
        import sys
        sys.exit()
 
    def loop(self):
        """Game main loop"""
        while self.gamestate:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.gamestate = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                   self.gamestate = False
                   
                print "Game nain loop"
                
        self.game_exit()

class MainGui(screen.Screen):
    pointer = False
    
    def __init__(self, **config):
        screen.Screen.__init__(self, **config)
        self.image.set_colorkey([255, 0, 255])
        
        global g
        import pointer
        self.pointer = pointer.Pointer(g.player)
            
    def blit_screen(self, window):
        global g
        
        import pygame, config
        text = pygame.font.Font(None, config.config()['text_size'])
        window.blit(text.render("Money "+str(g.player.score),    True, (255,0,0)), (500, 450))
        window.blit(text.render("Level "+str(g.level.score),     True, (255,0,0)), (500, 475))
        window.blit(text.render("Time  "+str(g.level.seconds()), True, (255,0,0)), (500, 500))
        pygame.draw.circle(window, (255, 255, 255), (226, 487), 65)
        window.blit(text.render(str(g.player.shots),             True, (255,0,0)), (200, 475))
        
        if(self.pointer):
            window.blit(*self.pointer.move())

def init_gui(config):
    global screen_data, gui

    print "INIT GUI"
    print config
    screen_data = config.screens
    
    gui = PygameWin(
        screen_size = (800, 600),
        title       = u'Проверка',
        icon        = config.window['icon'],
        main_theme  = config.main_theme
    )
    
def init_game(game):
    global p, i, g, screen_data
    import pointer
    g = game
    i = MainGui(**screen_data['gui'])
    
def win():
    global gui, screen_data
    
    s = screen.Screen(**screen_data['win'])
    s.show_screen(gui.surface)

def loose():
    global gui, screen_data
    
    s = screen.Screen(**screen_data['loose'])
    s.show_screen(gui.surface)

def main():
    return 0

if __name__ == '__main__':
    main()

