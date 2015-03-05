#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.py
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
        
class Game():    
    lost = False
    win  = False
    
    def __init__(self, config = False):
        self.config = config

        import player
        self.player  = player.Player(config)
        
    def levelup(self):
        import level
        self.player.levelup()

    def win(self):
        print 'You win'
        self.win = True
    
    def loose(self):
        print 'You loose'
        self.lost = True
        
    def stop(self):
        print 'Player stop'
        self.loose()

def main():
    return 0

if __name__ == '__main__':
    main()
