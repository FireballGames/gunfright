#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mainloop.py
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

class Level():
    time        = 3000
    percent_bag = 2
    
    def __init__(self, game, config):
        import pygame
        self.time        = config['time']
        self.percent_bag = config['percent_bag']
        self.score       = config['score']
        self.speedrange  = config['speedrange']

        self.game  = game
        self.timer = pygame.time.Clock()

        self.background  = pygame.image.load(config['background'])
        self.moneybag    = pygame.image.load("res/money.png")
        self.moneybag.set_colorkey([255, 0, 255])

    def finish(self):
        self.time -= self.timer.tick()
        return self.time <= 0
        
    def can_add_bag(self):
        import random
        return random.randrange(100) < self.percent_bag
        
    def seconds(self):
        return self.time / 1000
        
    def dir(self):
        import random
        return [
            random.randrange(*self.speedrange['x']), 
            random.randrange(*self.speedrange['y'])
        ]

def show(game):
    import gui, pygame, time
    
    while not game.lost:
        game.player.levelup()
    
        level = dict(
            score       = game.player.next_lev,
            time        = 30000,
            percent_bag = 5,
            background  = 'res/town.png',
            speedrange  = {
                'x': [-10, 10],
                'y': [  5, 20],
            }
        )
        
        print game.lost
    
        import nextlev
        nextlev.show(game)

        import shootmoney
        shootmoney.show(game, Level(game, level))
    

def main():
    import game
    
    game = Game()
    show(game)
    return 0

if __name__ == '__main__':
    main()

