#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tile.py
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

class Tile():
    pos      = [0, 0, 0]
    rotation = [0.0, 0.0, 0.0, 0.0]
    scale    = 1.0
        
    def __init__(self, texture):
        self.texture = texture
        
    def rotate(self, angle, *axles):
        self.rotation[0] += angle
        self.rotation[1]  = axles[0]
        self.rotation[2]  = axles[1]
        self.rotation[3]  = axles[2]
        
    def draw(self):
        self.texture.draw(self.pos, rotate = self.rotation, scale = self.scale)

def main():
    return 0

if __name__ == '__main__':
    main()

