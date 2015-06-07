#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sound.py
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

import pygame

def init_sound(main_theme):
    pygame.mixer.init()
    pygame.mixer.music.load(main_theme)
    pygame.mixer.music.play()

def play(sound):
    print("Playing sound "+sound)
    pygame.mixer.Sound(sound).play()

def play_intro():
    print('Playing intro')
    # pygame.mixer.Sound("Data/Sounds/menu.wav").play()

def play_shoot():
    print('Playing shoot')
    pygame.mixer.Sound('res/sounds/shot.wav').play()

def play_hit():
    print('Playing hit')
    # pygame.mixer.Sound('res/sounds/hit.mp3').play()

def play_loose():
    print('Playing loose')
     # pygame.mixer.Sound("Data/Sounds/risa.wav").play()

def main():
    return 0

if __name__ == '__main__':
    main()
