import pygame
from .screen import Screen

i = None
g = None
gui = None
res = None

screen_data = {}


class MainGui(screen.Screen):
    pointer = False

    def __init__(self, **config):
        screen.Screen.__init__(self, **config)
        self.image.set_colorkey([255, 0, 255])

        global g
        from .pointer import Pointer
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


def win():
    global gui, screen_data

    s = screen.Screen(**screen_data['win'])
    s.show_screen(gui.surface)


def loose():
    global gui, screen_data

    s = screen.Screen(**screen_data['loose'])
    s.show_screen(gui.surface)
