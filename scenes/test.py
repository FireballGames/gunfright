#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
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

def screen_intro():
    print "Gunfright intro"
    return True
    
def screen_level(player):
    print "Level %s"%(player.level)
    return True

import bountyshooter, seekbandit, banditshooter

class Player():
    def __init__(self):
        self.level = 1
        self.shots = 6
        self.lives = 5
        self.score = 100
        self.pos   = [0, 0]
        self.dir   = 0
        
    def levelup(self):
        self.level += 1
        
    def shoot(self, pos, targets, d=10):
        if self.shots < 1: 
            print "Empty!!!"
            return False
        self.shots -= 1
        hits = []
        for target in targets:
            if (abs(pos[0]-target[0]) < d) and \
                (abs(pos[1]-target[1]) < d):
                hits.append(target)

        is_hit = len(hits)>0
        print "Shot %s - %s"%(str(pos), is_hit)
                    
        for hit in hits:
            self.score += 100
            hit[1] = -1
            
        return is_hit

    def reload(self):
        print "Reloading"
        self.shots = 6
        
    def move(self, d):
        self.dir = d
        if d==0: m = ( 1,  0)
        if d==1: m = ( 0,  1)
        if d==2: m = (-1,  0)
        if d==3: m = ( 0, -1)
        
        self.pos[0] += m[0]
        self.pos[1] += m[1]
        
        if self.pos[0] <  0: self.pos[0] =  0
        if self.pos[0] > 90: self.pos[0] = 90
        if self.pos[1] <  0: self.pos[1] =  0
        if self.pos[1] > 90: self.pos[1] = 90
        
    def seek(self, bandit):
        dx = bandit.pos[0]-self.pos[0]
        dy = bandit.pos[1]-self.pos[1]
        
        if (dx==0)and(abs(dy)<8):
            return True
        if (dy==0)and(abs(dx)<8):
            return True
        
        if abs(dx) > abs(dy):
            if dx>0:
                self.move(0)
            else:
                self.move(2)
        else:
            if dy>0:
                self.move(1)
            else:
                self.move(3) 
        
        return False
    
    def loose(self):
        self.lives -= 1
        return False

def main():
    print "-----------------------------------------------------------"

    play   = screen_intro()
    player = Player()
    while play:
        play = screen_level(player)
        if not play: break
        print "--------------------"
        
        play = bountyshooter.test(player)
        if not play: break
        print "--------------------"

        found = False
        while play and (not found):
            found = seekbandit.test(player)
            play  = (player.lives > 0)
            if not play: break
            if not found: continue
            
            found = banditshooter.test(player)
            play  = (player.lives > 0)
            if not play: break

            player.levelup()
    print "-----------------------------------------------------------"
    return 0

if __name__ == '__main__':
    main()

