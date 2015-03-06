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

from d2lib.config import *
import gui.scene, gui.text

class NextLev(gui.scene.SceneConfig):
    def __init__(self, game):
        scene_config = Config().screen('nextlev')
        gui.scene.SceneConfig.__init__(self, **scene_config)
        self.game = game
        
    def init_controls(self, screen):
        font      = screen.create_font( None, 32, True)
        self.text = gui.text.Text(font, (1.0, 1.0, 1.0))

        self.screen.gui.append(self.text)
    
    def get_level(self):
        return self.game.player.level
        
    def draw(self):
        self.text.set_text("LEVEL %s"%(self.get_level()))

        gui.scene.SceneConfig.draw(self)
        
def main():
    return 0

if __name__ == '__main__':
    main()
