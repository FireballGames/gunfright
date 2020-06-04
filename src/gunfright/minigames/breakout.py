import pygame
import random
from datetime import datetime, timedelta
from v2.d2game import Game
from v2.d2game.game_object import GameObject
from v2.d2game.text_object import TextObject


class Brick(GameObject):
    def __init__(self, bounds, color, effect=None, **options):
        super().__init__(bounds, (0, 0), **options)
        self.color = color
        self.effect = effect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)


class Ball(GameObject):
    def __init__(self, x, y, r, color, speed, **options):
        super().__init__(
            (x - r, y - r, r * 2, r * 2),
            speed,
            **options,
        )
        self.r = r
        self.d = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.r)

    def intersect(self, item):
        edges = {
            'left': pygame.Rect(item.left, item.top, 1, item.height),
            'right': pygame.Rect(item.right, item.top, 1, item.height),
            'top': pygame.Rect(item.left, item.top, item.width, 1),
            'bottom': pygame.Rect(item.left, item.bottom, item.width, 1),
        }
        collisions = set(edge for edge, rect in edges.items() if self.bounds.colliderect(rect))

        if not collisions:
            return None
        elif len(collisions) == 1:
            return list(collisions)[0]
        elif 'top' in collisions:
            if self.centery >= item.top:
                return 'top'
            return 'left' if self.centerx < item.left else 'right'
        elif 'bottom' in collisions:
            if self.centery >= item.bottom:
                return 'bottom'
            return 'left' if self.centerx < item.left else 'right'
        else:
            return None


class Paddle(GameObject):
    LEFT = 0
    RIGHT = 1

    def __init__(self, bounds, color, offset, **options):
        super().__init__(bounds, (0, 0), **options)
        self.color = color
        self.offset = offset
        self.direction = None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def on_key(self, event):
        if event.type == pygame.K_LEFT:
            self.direction = None if self.direction == self.LEFT else self.LEFT
        elif event.type == pygame.K_RIGHT:
            self.direction = None if self.direction == self.RIGHT else self.RIGHT

    def update(self):
        if self.direction == self.LEFT:
            self.move(-(min(self.offset, self.left)), 0)
        elif self.direction == self.RIGHT:
            self.move(min(self.offset, self.options.get('screen_width', 800) - self.right), 0)
        else:
            return


class Button(GameObject):
    PRESSED = 1
    HOVER = 2
    NORMAL = 3

    def __init__(
        self,
        bounds,
        text,
        on_click=lambda x: None,
        padding=0,
        **options,
    ):
        super().__init__(bounds, (0, 0), **options)
        self.state = self.NORMAL
        self.on_click = on_click
        self.__background_colors = {
            self.NORMAL: self.options.get('button_color_normal', (255, 255, 0)),
            self.HOVER: self.options.get('button_color_hover', (255, 255, 0)),
            self.PRESSED: self.options.get('button_color_pressed', (255, 255, 0)),
        }
        self.text = TextObject(
            self.bounds.left + padding,
            self.bounds.top + padding,
            lambda: text,
            self.options.get('button_text_color', (0, 0, 255)),
            self.options.get('font_name', 'Arial'),
            self.options.get('font_size', 25),
        )

    @property
    def background_color(self):
        return self.__background_colors.get(self.state, (0, 0, 0))

    def draw(self, surface):
        pygame.draw.rect(surface, self.background_color, self.bounds)
        self.text.draw(surface)

    def on_mouse_move(self, event):
        if self.bounds.collidepoint(event.pos):
            if self.state != self.PRESSED:
                self.state = self.HOVER
        else:
            self.state = self.NORMAL

    def on_mouse_button_down(self, event):
        if self.bounds.collidepoint(event.pos):
            self.state = self.PRESSED

    def on_mouse_button_up(self, event):
        if self.state == self.PRESSED:
            self.on_click(self)
            self.state = self.HOVER


class Breakout(Game):
    class Resources:
        def __init__(self, background_filename):
            if background_filename:
                self.background = pygame.image.load(background_filename)
            else:
                self.background = None

            pygame.mixer.pre_init(44100, 16, 2, 4096)
            pygame.font.init()

            self.sound_effects = {
                'brick_hit': pygame.mixer.Sound('res/brick_hit.wav'),
                'paddle_hit': pygame.mixer.Sound('res/paddle_hit.wav'),
            }
            self.music = pygame.mixer.music.load('res/music.mp3')
            pygame.mixer.music.play(-1, 0.0)

    def __init__(self, window, player, **options):
        super().__init__(window, player, **options)
        self.objects = []
        self.menu_items = []

        self.res = self.Resources(
            background_filename=options.get('background'),
        )

        self.lives = 3
        self.ball = None
        self.paddle = Paddle(
            pygame.Rect(0, 0, 10, 10),
            (0, 255, 0),
            5,
        )
        self.bricks = []
        self.score = 0
        self.points_per_brick = 5
        self.start = False

        self.window.quit_handlers.append(lambda: self.window.close())
        self.window.keydown_handlers[pygame.K_LEFT].append(self.paddle.on_key)
        self.window.keydown_handlers[pygame.K_RIGHT].append(self.paddle.on_key)
        self.window.keyup_handlers[pygame.K_LEFT].append(self.paddle.on_key)
        self.window.keyup_handlers[pygame.K_RIGHT].append(self.paddle.on_key)
        self.window.update_handlers.append(self.update)
        self.window.draw_handlers.append(self.draw)

        self.effects = {
            'long_paddle': (
                (255, 128, 0),
                lambda g: g.paddle.bounds.inflate_ip(self.options.get('paddle_width', 10) // 2, 0),
                lambda g: g.paddle.bounds.inflate_ip(-self.options.get('paddle_width', 10) // 2, 0),
            ),
            'slow_ball': (
                (0, 255, 255),
                lambda g: g.change_ball_speed(-1),
                lambda g: g.change_ball_speed(1),
            ),
            'triple_points': (
                (0, 255, 128),
                lambda g: g.set_points_per_brick(3),
                lambda g: g.set_points_per_brick(1),
            ),
            'extra_life': (
                (128, 128, 0),
                lambda g: g.add_life(),
                lambda g: None,
            ),
        }
        self.reset_effect = None
        self.effect_start_time = None

    def create_ball(self):
        speed = (random.randint(-2, 2), self.options.get('ball_speed', 10))
        self.ball = Ball(
            self.options.get('screen_width', 800) // 2,
            self.options.get('screen_height', 600) // 2,
            self.options.get('ball_radius', 10),
            self.options.get('ball_color', (255, 0, 0)),
            speed,
        )
        self.objects.append(self.ball)

    def create_menu(self):
        for menu_item_id, (text, on_click) in enumerate((
            ('PLAY', self.on_play),
            ('QUIT', self.on_quit),
        )):
            button = Button(
                (
                    self.options.get('menu_offset_x', 2),
                    self.options.get('menu_offset_y', 2) + (self.options.get('menu_button_h', 2) + 5) * menu_item_id,
                    self.options.get('menu_button_w', 2),
                    self.options.get('menu_button_h', 2),
                ),
                text,
                on_click,
                padding=5,
            )
            self.objects.append(button)
            self.window.mouse_move_handlers.append(button.on_mouse_move)
            self.window.mouse_button_up_handlers.append(button.on_mouse_button_up)
            self.window.mouse_button_down_handlers.append(button.on_mouse_button_down)

    def create_bricks(self):
        w = self.options.get('brick_width', 10)
        h = self.options.get('brick_height', 5)
        brick_count = self.options.get('screen_width', 800) // (w + 1)
        offset_x = (self.options.get('screen_width', 800) - brick_count * (w + 1)) // 2

        bricks = []
        for row in range(self.options.get('row_count', 5)):
            for col in range(brick_count):
                effect = None
                brick_color = self.options.get('brick_color', (255, 255, 255))
                index = random.choice(self.effects.keys())
                x = self.effects[index]
                brick_color = x[0]
                effect = x[1:]
                brick = Brick(
                    pygame.Rect(
                        offset_x + col * (w + 1),
                        self.options.get('offset_y', 2) + row * (h + 1),
                        w,
                        h,
                    ),
                    brick_color,
                    effect,
                )
                bricks.append(brick)
                self.objects.append(brick)
        self.bricks = bricks

    def on_play(self, button):
        for b in self.menu_items:
            self.objects.remove(b)
        self.start = True

    def on_quit(self, button):
        self.running = False

    def show_message(
        self,
        text,
        color=(255, 255, 255),
        font_name='Arial',
        font_size=20,
        center=False,
    ):
        message = TextObject(
            self.options.get('screen_width', 800) // 2,
            self.options.get('screen_height', 600) // 2,
            lambda: text,
            color,
            font_name,
            font_size,
        )
        self.draw()
        message.draw(self.window.surface, center)
        pygame.display.update()
        pygame.time.sleep(self.options.get('message_duration', 1000))

    def update(self):
        for o in self.objects:
            o.update()

        if not self.bricks:
            self.show_message('YOU WIN!!!', center=True)
            self.running = False
            return

        if self.reset_effect:
            elapsed = datetime.now() - self.effect_start_time
            if elapsed >= timedelta(seconds=self.options.get('effect_duration', 15)):
                self.reset_effect(self)
                self.reset_effect = None

    def draw(self):
        self.window.surface.blit(self.res.background, (0, 0))
        for o in self.objects:
            o.draw(self.window.surface)

    def run(self):
        while self.running:
            self.window.update()

    def collisions(self):
        s = self.ball.speed

        edge = self.ball.intersect(self.paddle)
        if edge is not None:
            self.res.sound_effects['paddle_hit'].play()
        if edge == 'top':
            if self.paddle.direction == self.paddle.LEFT:
                self.ball.speed = (s[0] - 1, -s[1])
            elif self.paddle.direction == self.paddle.RIGHT:
                self.ball.speed = (s[0] + 1, -s[1])
            else:
                self.ball.speed = (s[0], -s[1])
        elif edge in ('left', 'right'):
            self.ball.speed = (-s[0], s[1])

        if self.ball.top > self.options.get('screen_height', 600):
            self.lives -= 1
            if self.lives == 0:
                self.running = False
            else:
                self.create_ball()
        if self.ball.top < 0:
            self.ball.speed = (s[0], -s[1])
        if self.ball.left < 0 or self.ball.right > self.options.get('screen_width', 800):
            self.ball.speed = (-s[0], s[1])

        if not self.bricks:
            self.show_message('YOU WIN!!!', center=True)
            self.running = False
            return

        for brick in self.bricks:
            edge = self.ball.intersect(brick)
            if not edge:
                continue

            self.res.sound_effects['brick_hit'].play()

            if brick.effect is not None:
                if self.reset_effect is not None:
                    self.reset_effect(self)
                self.effect_start_time = datetime.now()
                brick.effect[0](self)
                self.reset_effect = brick.effect[1]

            self.bricks.remove(brick)
            self.objects.remove(brick)
            self.score += self.points_per_brick

            if edge in ('top', 'bottom'):
                self.ball.speed = (s[0], -s[1])
            else:
                self.ball.speed = (-s[0], s[1])
