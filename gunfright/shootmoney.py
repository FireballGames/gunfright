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

import gui.scene, gui.opengl, gui.opengl.tile, pygame.time

class Bounties():
    def __init__(self, textures):
        self.textures = textures
        self.bounties = []
        
        self.timer   = pygame.time.Clock()
        self.ticks   = -1
        self.tpf     = 50
        
    def add_bounty(self, b):
        if b:
            m = Moneybag(self.textures[0])
            self.bounties.append(m)
            # Moneybag(self.moneybag, b, {
            #     'rect': self.rect.copy(),
            #     'tpf':  100
            # })
            return m
        return None

        
    def draw(self):
        for b in self.bounties: b.draw()
        self.ticks += self.timer.tick()
        if self.ticks >= self.tpf:
            self.ticks = 0
            for b in self.bounties: b.move()
            self.bounties = [b for b in self.bounties if b.pos[1] > 0]
        
    def shoot(self, player, mouse):
        rpos = (
            mouse.pos[0] - mouse.texture.pos[0],
            mouse.pos[1] - mouse.texture.pos[1],
            mouse.pos[2] - mouse.texture.pos[2],
        )
        print rpos
        for b in self.bounties:
            print [b.pos]
            if (b.pos[0] in range(rpos[0]-100, rpos[0]+100)) and \
                (b.pos[1] in range(rpos[1]-100, rpos[1]+100)):
                    b.pos[1] = 400
                    player.score += 100
        pass
        
class Moneybag(gui.opengl.tile.Tile):
    def __init__(self, texture):
        gui.opengl.tile.Tile.__init__(self, texture)
        
        import random
        
        self.pos = [
            random.randrange(-400, 400),
            300,
            -250, # random.randrange( 150, 450)
        ]
        self.dir = (
            random.randrange(-10, 10),
            random.randrange( 10, 20),
            0 # random.randrange(-10, 10)
        )
        
    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
        self.pos[2] += self.dir[2]            
            
        if self.pos[1] < 0:
            del self
            return False
            
        return True


class ShootMoney(gui.scene.SceneConfig):
    def __init__(self, game, **config):
        gui.scene.SceneConfig.__init__(self, **config)
        
        self.game = game
        # self.create_gui(self.create_texture('res/gui.png'))
        
    def init_controls(self, screen):
        self.moneybag  = screen.create_texture("res/money.png")

        self.bounties = Bounties([self.moneybag])
        self.controls.append(self.bounties)           
        
        font      = screen.create_font( None, 32, True)
        self.shots_text     = gui.text.Text(font, (1.0, 1.0, 1.0))
        self.shots_text.pos = (-300, 100)
        screen.gui.append(self.shots_text)   
        self.score_text = gui.text.Text(font, (1.0, 1.0, 1.0))
        self.score_text.pos = (100, 100)
        screen.gui.append(self.score_text)   

    def draw(self):
        b = self.bounties.add_bounty(self.game.level.add_bounty())
        # self.screen.tiles.append(b)
            
        self.shots_text.set_text("SHOTS %s"%(self.get_shots()))
        self.score_text.set_text("SCORE %s"%(self.game.player.score))

        gui.scene.SceneConfig.draw(self)
        
    def process_event(self, event):
        gui.scene.SceneConfig.process_event(self, event)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print "click"
            #if self.in_active() and self.player.shoot():
            if self.game.player.shoot():
                # sound.play_shoot()
                self.bounties.shoot(self.game.player, self.screen.mouse_tile)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print "reload"
            self.game.player.reload()
        
    def get_shots(self):
        return self.game.player.shots

def main():
    return 0

if __name__ == '__main__':
    main()

