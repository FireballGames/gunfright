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

import pygame
import screen

i = None
g = None
gui = None
res = None

screen_data = {}


class PygameWin():
    def __init__(self, **args):
        self.state = True
        self.main_theme = None
        self.screen_size = [800, 600]

        pygame.init()
        self.init_window(**args)

        if 'main_theme' in args:
            self.main_theme = args['main_theme']

        if self.main_theme:
            import sound
            sound.init_sound(self.main_theme)

    def init_window(self, **args):
        # Setting default values
        flag = pygame.DOUBLEBUF

        # Loading values from args
        # screen_data = config['screens']
        if 'screen_size' in args:
            self.screen_size = args['screen_size']
        if 'flag' in args:
            flag = args['flag']

        # Setting display mode
        self.surface = pygame.display.set_mode(self.screen_size, flag)

        # Other window options
        if 'title' in args:
            pygame.display.set_caption(args['title'].encode("utf8"))
        if 'icon' in res.args():
            pygame.display.set_icon(res.load('icon', alpha=True))
        if 'show_mouse' in args:
            pygame.mouse.set_visible(iargs['show_mouse'])

        return self.surface


class MainGui(screen.Screen):
    pointer = False

    def __init__(self, **config):
        screen.Screen.__init__(self, **config)
        self.image.set_colorkey([255, 0, 255])

        global g
        import pointer
        self.pointer = pointer.Pointer(g.player)

    def blit_screen(self, window):
        global g

        import pygame
        text = res.text()
        window.blit(text.render("Money "+str(g.player.score),    True, (255, 0, 0)), (500, 450))
        window.blit(text.render("Level "+str(g.level.score),     True, (255, 0, 0)), (500, 475))
        window.blit(text.render("Time  "+str(g.level.seconds()), True, (255, 0, 0)), (500, 500))
        pygame.draw.circle(window, (255, 255, 255), (226, 487), 65)
        window.blit(text.render(str(g.player.shots),             True, (255, 0, 0)), (200, 475))

        if(self.pointer):
            window.blit(*self.pointer.move())


def init_gui(config):
    global screen_data, gui

    print "INIT GUI"
    print config
    screen_data = config.screens

    gui = PygameWin(
        screen_size = (800, 600),
        title = u'Проверка',
        icon = config.window['icon'],
        main_theme = config.main_theme
    )


def init_game(game):
    global p, i, g, screen_data
    g = game
    i = MainGui(**screen_data['gui'])


def win():
    global gui, screen_data

    s = screen.Screen(**screen_data['win'])
    s.show_screen(gui.surface)


def loose():
    global gui, screen_data

    s = screen.Screen(**screen_data['loose'])
    s.show_screen(gui.surface)


def main():
    return 0

if __name__ == '__main__':
    main()
