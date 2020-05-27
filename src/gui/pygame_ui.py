import pygame
import sys
from .sound import init_sound


class PygameUi:
    __res = None

    def __init__(self, **args):
        self.state = True
        self.main_theme = None
        self.screen_size = [800, 600]

        pygame.init()
        self.init_window(**args)

        # if 'main_theme' in args:
        #     self.main_theme = args['main_theme']

        # if self.main_theme:
        #    init_sound(self.main_theme)

    def init_window(self, **args):
        version = sys.version_info

        # Setting default values
        flag = pygame.DOUBLEBUF

        print(args)

        # Loading values from args
        # screen_data = config['screens']
        if 'size' in args:
            self.screen_size = args['size']
        if 'flag' in args:
            flag = args['flag']
        title = args['title']
        if version[0] < 3 :
            title = title.encode("utf8")

        # Setting display mode
        self.surface = pygame.display.set_mode(self.screen_size, flag)

        # Other window options
        if 'title' in args:
            pygame.display.set_caption(title)
        if 'icon' in self.__res.args():
            pygame.display.set_icon(self.__res.load('icon', alpha=True))
        if 'show_mouse' in args:
            pygame.mouse.set_visible(args['show_mouse'])

        return self.surface

    def clear(self):
        self.surface.fill((0, 0, 0))

    def draw_image(self, image, pos=(0, 0)):
        self.surface.blit(image, pos)

    def draw(self):
        pygame.display.flip()
