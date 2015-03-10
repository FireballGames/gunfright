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

ticks = 20
speed = 10
throw = 50

p_shoot  = 30
p_reload = 75
    
def player_shoot(player, targets):
    shot  = (random.randrange(100), random.randrange(100))
    player.shoot(shot, targets)
    
def player_reload(player):
    if random.randrange(6) > player.shots:
        player.reload()
    
def test(player):
    global ticks, speed, throw
    global p_shoot, p_reload
    
    print "Bounties"
    bounties = []
    for i in range(ticks):
        bounties = [bounty for bounty in bounties if bounty[1] > 0]
        
        for bounty in bounties: bounty[1] -= speed
        
        if random.randrange(100) > throw:   bounties.append([random.randrange(100), 100])
        if random.randrange(100) > p_shoot: player_shoot(player, bounties)
        if player.shots < 2:                player_reload(player) 
        
        data = {
            'shots':    player.shots,
            'score':    player.score,
            'bounties': bounties
        }
        print "%s: %s"%(i, data)
    return True

def main():
    return 0

if __name__ == '__main__':
    main()

