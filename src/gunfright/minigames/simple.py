import pygame
import gui
import gui.controls
import screens.shootmoney
from d2game import states
from d2game.game import Game
from log import logger
from ..level import ShootBounty


class Simple(Game):
    def __init__(self, player, config):
        super().__init__(config)

        logger.debug("Simple game")

        self.player = player
        self.controls = {}
        self.screen = None
        self.level = None

    def run(self):
        logger.debug("Running simple game")
        # gui.g = self
        # self.play_sound()
        # self.load_level(self.player.level)

        super().run()

        # self.player.bonus = False
        return states.LOOSE

    def on_play(self):
        # gui.gui.clear()

        super().on_play()

        # self.screen.show_image(gui.gui.surface)

        # pygame.display.flip()
        # pygame.time.delay(2)
        # # self.screen.show_screen(gui.gui.surface)

        # if not self.screen.showing:
        #     self.set_state(states.WIN)

    def process_event(self, event):
        super().process_event(event)

        # self.screen.interface.pointer.process_event(event, screens.shootmoney.moneybags)

    def load_level(self, level):
        logger.debug("Loading level %s" % (level))

        level_data = self.config.level(level)
        level_screen = self.config.get_screen('shootmoney')
        level_screen.update({
            'background': level_data["background"],
            'interface':  gui.i
        })

        if level_data['type'] == 'bounty':
            level_data['player'] = self.player
            self.level = ShootBounty(**level_data)
        else:
            self.level = None

        if not self.player.bonus:
            return

        self.screen = screens.shootmoney.ShootMoney(**level_screen)
        self.screen.init_win()

    def draw(self):
        self.controls['main'].show()
        self.controls['shots'].show(self.player.shots)
        self.controls['lives'].show(self.player.lives)
        self.controls['score'].show(self.player.score)
