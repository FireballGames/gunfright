#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  view.py
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

import game, pygame, gui.opengl

class View():
    def __init__(self, config = None):
        import screens.intro
        
        print "Initialization game"
        self.config = config
        print self.config
        
        gui_config = self.config.window
        gui_config['main_theme'] = self.config.main_theme
        gui_config['show_mouse'] = True
        
        if self.config.opengl:
            if not('flag' in gui_config): gui_config['flag'] = pygame.DOUBLEBUF
            gui_config['flag'] |= pygame.OPENGL
            self.gui = gui.opengl.OpenGLWin(**gui_config)
        else:
            self.gui = gui.PygameWin(**gui_config)
            
        print "Show intro screen"
        scene = screens.intro.Intro()
        self.gui.create_screen(scene)
        self.gui.show()
        
    def run(self, g):
        # import screens.nextlev, screens.shootmoney
        # game.levelup()
        
        import screens.nextlev, shootmoney
        
        scene = screens.nextlev.NextLev(g)
        s     = self.gui.only_screen(scene)

        print "New level"
        self.gui.show()
        
        c = self.config.screens['shootmoney'].copy()
        # c.update({
        #     'view_box': (
        #         -400, 400,
        #           0, 600,
        #           0, 600,
        #    )
        # })
        scene = shootmoney.ShootMoney(g, **c)
        s     = self.gui.only_screen(scene)

        print "Shoot money"
        self.gui.show()

        c = self.config.screens['seekbandit'].copy()
        scene = gui.scene.SceneConfig(**c)
        s     = self.gui.only_screen(scene)

        print "Seek bandit"
        self.gui.show()

        c = self.config.screens['shootbandit']
        scene = shootmoney.ShootMoney(g, **c)
        s     = self.gui.only_screen(scene)
        
        print "Shoot bandit"
        self.gui.show()
        
    def is_running(self, game):
        running = self.gui.gamestate and game.is_running
        if not running: game.loose
        return running


def main():
    return 0

if __name__ == '__main__':
    main()

