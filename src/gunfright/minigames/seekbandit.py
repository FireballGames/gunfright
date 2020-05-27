"""
Seek bandit minigames
"""
import pygame
import d2game.map
import gui
from config import Config
from d2game.game import Game
from log import logger
# from ..level import ShootBounty


class SeekBandit(Game):
    def __init__(self, player, params):
        super().__init__(params)

        logger.info("Seek bandit minigames")

        self.player = player
        self.map = d2game.map.Map((16, 16))
        logger.debug(self.player.pos)

        self.controls = {
            'main': gui.controls.ControlShoot(
                pos = (1, 1),
                size = (100, 100)
            ),
            'shots': gui.controls.ControlImageList(
                gui.controls.ControlImage('Revolver'),
                pos = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6))
            ),
            'lives': gui.controls.ControlImageList(
                gui.controls.ControlImage('Hat'),
                pos = ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1))
            ),
            'score': gui.controls.ControlText(
                '$%s',
                pos = (0, 0),
                size = 16
            ),
            'map': gui.controls.ControlText(
                '(%s)',
                pos = (400, 0),
                size = 16
            ),
            'player': gui.controls.MapPlayer({
                "pos": [400, 300],
                "image": "player",
                "map": self.map,
            })
        }
        self.screen = None
        self.gui = gui.res.load("gui")

    def run(self):
        logger.debug("Running bandit seeker")

        gui.g = self

        self.load_level(self.player.level)
        d2game.game.Game.run(self)

    def play(self):
        gui.gui.clear()

        d2game.game.Game.play(self)

        bandit = None
        if self.player.seek(bandit):
            self.win()
            return

        self.draw()

        pygame.display.flip()
        pygame.time.delay(2)

    def load_level(self, level):
        level_data = Config.level(level)

        self.map.generate_map((16, 16))
        self.player.pos = [len(self.map.map_array)/2 - 2, len(self.map.map_array[0])/2 + 2]
        # global people, bandit
        # bandit = People(random.randrange(size_x*5), random.randrange(size_y*5))

    def move_objects(self):
        # global people, bandit
        # for p in people:
        #    # p.move(random.randrange(4))
        #    # if (p.pos[0]==player.pos[0])and(p.pos[1]==player.pos[1]):
        #        # print 'Hit by people'
        #        # return player.loose()
        #    # print p.pos
        # bandit.move(random.randrange(4))
        pass

    def draw_map(self):
        # draw_map(player.pos[0], player.pos[1], 8, 8)
        for i in range(len(self.map.map)):
            row = self.map.map[i]
            for j in range(len(row)):
                pass
                # im = self.map.draw((i, j))
                # if im is not None:
                #     self.window.draw_image(im)
        pass

    def draw(self):
        # self.draw_map()
        self.controls['player'].pos = self.player.pos
        self.controls['player'].show()

    def draw_controls(self):
        logger.debug({
            'player': self.player.pos,
            'score':  self.player.score,
            'shots':  self.player.shots,
            'lives':  self.player.lives
        })
        return

    def move_and_draw(self, direction):
        self.player.move(direction, self.map)
        self.draw_controls()

    def process_events(self):
        d2game.game.Game.process_events(self)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_and_draw(d2game.map.DIR_UP)
        if keys[pygame.K_DOWN]:
            self.move_and_draw(d2game.map.DIR_DOWN)
        if keys[pygame.K_LEFT]:
            self.move_and_draw(d2game.map.DIR_LEFT)
        if keys[pygame.K_RIGHT]:
            self.move_and_draw(d2game.map.DIR_RIGHT)
