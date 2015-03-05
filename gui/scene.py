#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scene.py
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

class SceneConfig():
    LIFETIME  = pygame.USEREVENT + 1
    
    def __init__(self, **config):
        print "SCENE"
        print config
        self.config = config

        self.controls = []
        
        self.m_pos     = [0, 0]
        self.gamestate = True

        self.sleep = False
        if "sleep" in config: self.sleep = config["sleep"]

        # Getting viewer position
        self.depth = [800, 600, 600]
        if "depth" in config: self.depth = config['depth']
        
        self.pos = [0, 0, -self.depth[2]/2]
        if "pos" in config: self.pos = config['pos']
        
        pygame.time.set_timer(self.LIFETIME, self.sleep*1000)

        # Deprecated
        
        # self.showing   = False
        # self.interface = False
        # if "showing"   in self.config: self.showing   = self.config["showing"]
        # if "interface" in self.config: self.interface = self.config["interface"]
        # if self.interface: self.interface.pointer.active = True
    
    def init_controls(self, screen):
        pass
        
    def draw(self):
        for c in self.controls:
            c.draw()
        
    def get_viewbox(self):
        return (self.pos[0]-self.depth[0]/2, self.pos[0]+self.depth[0]/2,
            self.pos[1]+self.depth[1]/2, self.pos[1]-self.depth[1]/2,
            self.pos[2]-self.depth[2]/2, self.pos[2]+self.depth[2]/2)

    def get_bg_pos(self):
        return (self.pos[0], self.pos[1], self.pos[2]+self.depth[2])
        
def main():
    return 0

if __name__ == '__main__':
    main()

