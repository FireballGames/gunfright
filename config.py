#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
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

class Config():
    __params = {}
    
    def __init__(self, filename = False):
        self.load(filename)

    def load(self, filename = False):
        if filename:
            import yaml
            self.__params.update(yaml.load(open(filename, 'r')))

    def __getitem__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False
    
    def __getattr__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False
    
    def __str__(self):
        return str(self.__params)
    
__config = Config()

def level(index):
    global __config
    levels = __config.levels
    if index in levels:
        return levels[index]
    else:
        return levels[-1]
        
def map():
    return [
        [1, 1, 2],
        [1, 2, 3],
        [2, 3, 3]
    ]

def config():
    global __config
    return __config

def screen(index):
    global __config
    return __config.screens[index]
    
def load(filename):
    global __config
    return __config.load(filename)

def main():
    global __config
    return __config

if __name__ == '__main__':
    main()
