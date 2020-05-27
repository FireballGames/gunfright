import pygame
import gui
import gui.controls
import screens.shootmoney
from config import Config
from d2game.game import Game
from ..level import ShootBounty


class BountyShooter(Game):
    def __init__(self, player, params):
        super().__init__(params)

        print("Shoot money minigames")
        self.player = player

        self.controls = {
            'main': gui.controls.ControlShoot(
                pos=(1, 1),
                size=(100, 100)
            ),
            'shots': gui.controls.ControlImageList(
                gui.controls.ControlImage('Revolver'),
                pos=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6))
            ),
            'lives': gui.controls.ControlImageList(
                gui.controls.ControlImage('Hat'),
                pos=((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1))
            ),
            'score': gui.controls.ControlText(
                '$%s',
                pos=(0, 0),
                size=16
            )
        }
        self.screen = None
        self.level = None

    def run(self):
        print("Running bounty shooter")
        gui.g = self

        # self.play_sound()
        self.load_level(self.player.level)
        super().run()

        self.player.bonus = False

    def play(self):
        gui.gui.clear()

        super().play()

        self.screen.show_image(gui.gui.surface)

        pygame.display.flip()
        pygame.time.delay(2)
        # self.screen.show_screen(gui.gui.surface)

        if not self.screen.showing:
            self.win()

    def process_event(self, event):
        super().process_event(event)

        self.screen.interface.pointer.process_event(event, screens.shootmoney.moneybags)

    def load_level(self, level):
        print("Loading level %s" % (level))

        level_data = Config.level(level)
        level_screen = Config.get_screen('shootmoney')
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
