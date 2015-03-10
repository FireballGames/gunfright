#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shootmoney.py
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

import controls

class Scene():
    def __init__(self):
        self.main = controls.ControlShoot(
            pos  = (1, 1),
            size = (100, 100)
        )
        
        self.shots = controls.ControlImageList(
            controls.ControlImage('Revolver'),
            pos = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
        )
        self.lives = controls.ControlImageList(
            controls.ControlImage('Hat'),
            pos = ((1,1),(2,1),(3,1),(4,1),(5,1),(6,1))
        )
        self.score = controls.ControlText(
            '$%s', 
            pos=(0, 0), 
            size=16
        )
        
    def show(self, player):
        self.main.show()
        self.shots.show(player.shots)
        self.lives.show(player.lives)
        self.score.show(player.score)

class Player():
    def __init__(self):
        self.shots = 6
        self.lives = 5
        self.score = 100

def main():
    p = Player()
    s = Scene()
    s.show(p)
    return 0

if __name__ == '__main__':
    main()

