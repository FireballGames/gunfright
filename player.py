#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  player.py
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

class Player():
    config  = {
        'levelups': [1000]
    }
    score   = 0
    level   = 0
    shots   = 6
    
    def __init__(self, config):
        if 'player' in config:
            self.player.config.update(config['player'])

        self.levelups = self.config['levelups']
            
    def levelup(self):
        if self.level >= len(self.levelups):
            new_lev = self.score + self.levelups[len(self.levelups) - 1]
            self.levelups.append(new_lev)
        self.level += 1
        self.next_lev = self.levelups[self.level - 1]
        
    def shoot(self):
        if(self.shots > 0):
            self.shots -= 1
            return True
        else:
            return False
        
    def reload(self):
        if self.score > 100:
            self.score -= 100
            self.shots =  6
    
def main():
    return 0

if __name__ == '__main__':
    main()

