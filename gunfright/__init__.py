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

import game

class Gunfright(game.Game):
    def __init__(self, config = None):
        game.Game.__init__(self, config)
        self.next_lev   = False
        self.is_running = True
        
    def win(self):
        game.Game.win(self)
        self.next_lev = True
        
        sdlgui.win()
        
    def loose(self):
        game.Game.loose(self)
        
        sdlgui.loose()
        
    def levelup(self):
        import game.level
        
        game.Game.levelup(self)

        print "Level up"
        print self.config
        
        level_data = self.config.level(self.player.level)
        level_data.update({
            'player': self.player
        })
        
        if level_data['type'] == 'bounty':
            self.level = game.level.ShootBounty(**level_data)

def main():
    g = Gunfright()
    return 0

if __name__ == '__main__':
    main()
