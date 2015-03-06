#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bountyshooter.py
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

import random

ticks  = 20
speed  = 10
bandit = [0, 0]

b_shoot  = 10
p_shoot  = 75
p_reload = 75
    
def player_shoot(player, bandit):
    shot  = (random.randrange(100), random.randrange(100))
    return player.shoot(shot, [bandit], 25)
    
def player_reload(player):
    if random.randrange(6) > player.shots:
        player.reload()
    
def test(player):
    global bandit, ticks, speed, throw
    global p_shoot, p_reload, b_shoot
    
    print "Duel"
    bandit = [random.randrange(100), random.randrange(100)]
    while True:
        bandit[0] += random.randrange(-speed, speed)
        bandit[1] += random.randrange(-speed, speed)
        if(bandit[0]<  0): bandit[0] =   0
        if(bandit[0]>100): bandit[0] = 100
        if(bandit[1]<  0): bandit[1] =   0
        if(bandit[1]>100): bandit[1] = 100
        
        if random.randrange(100) < b_shoot: 
            print "Shot by bandit"
            return player.loose()
        if random.randrange(100) < p_shoot: 
            if player_shoot(player, bandit):
                return True
        if player.shots < 2:                player_reload(player) 
        
        data = {
            'shots':  player.shots,
            'score':  player.score,
            'bandit': bandit
        }
        print "%s"%(data)

def main():
    return 0

if __name__ == '__main__':
    main()

