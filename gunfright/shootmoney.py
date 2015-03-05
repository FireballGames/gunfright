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

import gui.scene, gui.opengl, gui.opengl.tile

class Moneybag(gui.opengl.tile.Tile):
    def __init__(self, texture):
        gui.opengl.tile.Tile.__init__(self, texture)

        import random
        
        self.pos = [
            random.randrange(-400, 400),
            -300,
            random.randrange(-300, 300)
        ]
        self.dir = (
            random.randrange(-10, 10),
            random.randrange( 10, 20),
            random.randrange(-10, 10)
        )
        
    def move(self):
        # if self.ticks < 0:
        #    self.rect.x = self.box.x + random.randrange(self.box.width)
        #    self.rect.y = self.box.y
        #    self.ticks  = self.timer.tick()
        #    return [self.image, self.rect]
           
        # self.ticks += self.timer.tick()
        # if self.ticks >= self.tpf:
        #    self.ticks = 0
        #    self.rect.x += self.dir[0]
        #    self.rect.y += self.dir[1]
         
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
        self.pos[2] += self.dir[2]
            
        # print "Y"+str(self.pos[1])
        if self.pos[1] >= 300:
            del self

class ShootMoney(gui.scene.SceneConfig):
    def __init__(self, game, **config):
        gui.scene.SceneConfig.__init__(self, **config)
        
        self.game = game
        # self.create_gui(self.create_texture('res/gui.png'))
        
    def init_controls(self, screen):
        self.moneybag  = screen.create_texture("res/money.png")
        self.moneybags = []
        
        font      = screen.create_font( None, 32, True)
        self.text = gui.text.Text(font, (1.0, 1.0, 1.0))

        self.controls.append(self.text)   

    def draw(self):
        b = self.add_bounty()
        # self.screen.tiles.append(b)
            
        for m in self.moneybags:
            m.move()
            if m.pos[1] > 300: del m
                
        self.text.set_text("SHOTS %s"%(self.get_shots()))

        gui.scene.SceneConfig.draw(self)
        
    def get_shots(self):
        return self.game.player.shots

    def add_bounty(self):
        b = self.game.level.add_bounty() 
        if b:
            m = Moneybag(self.moneybag)
            self.moneybags.append(m)
            # Moneybag(self.moneybag, b, {
            #     'rect': self.rect.copy(),
            #     'tpf':  100
            # })
            self.controls.append(m)
            return m
        return None
        
    def d2_blit_screen(self, window):
        if game.lost:                return False;
        if game.level.is_finished(): return False;
        return self.showing
        
        txt = gui.text.Text(self.gui.fonts[0], (1.0, 1.0, 1.0))
        txt.set_text("SHOTS %s"%(g.player.shots))


def main():
    return 0

if __name__ == '__main__':
    main()

