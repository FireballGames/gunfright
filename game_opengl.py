#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  opengl.py
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

import gunfright, gunfright.view
from d2lib.config import Config

def main(config = None):
    if config is None: config = Config()
    
    v = gunfright.view.View(config)
    g = gunfright.Gunfright(config)
    
    print 'Starting game'
    while v.is_running(g):
        g.levelup()
        v.run(g)
    return 0

if __name__ == '__main__':
    config = Config('game.yml')
    config.set_opengl(True)
    main(config)

