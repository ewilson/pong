import pygame
from pygame.locals import *

HEIGHT = 600
WIDTH = 800
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = 0, 0, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 96
GREEN = 0, 255, 0
P_HEIGHT = 80
P_WIDTH = 10
BALL_START = WIDTH / 2, 50

pygame.mixer.init()


class Paddle(object):

    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
        self.delta = 10

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def move(self, direction):
        if self.has_room(direction):
            self.cleanup()
            self.rect = self.rect.move(0, direction * self.delta)
            pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def cleanup(self):
        pygame.draw.rect(DISPLAYSURF, BLACK, self.rect)

    def has_room(self, direction):
        if direction == 1:
            return HEIGHT - self.delta >= self.rect.bottom
        elif direction == -1:
            return self.delta <= self.rect.top


class Ball(object):

    def __init__(self, center, radius, color, delta):
        self.center = center
        self.radius = radius
        self.color = color
        self.delta = delta
        self.click = pygame.mixer.Sound("../paddle.wav")
        self.bounce = pygame.mixer.Sound("../bounce.wav")

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)

    def move(self):
        pygame.draw.circle(DISPLAYSURF, BLACK, self.center, self.radius)
        self.center = self.center[0] + self.delta[0], self.center[1] + self.delta[1]
        pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)

    def touch_top(self):
        return self.center[1] <= self.radius or self.center[1] >= HEIGHT - self.radius

    def touch_paddle(self, left_p, right_p):
        rect = self._rect()
        return left_p.rect.colliderect(rect) or right_p.rect.colliderect(rect)

    def bounce_wall(self):
        self.delta = (self.delta[0], -self.delta[1])
        self.bounce.play()

    def bounce_paddle(self, left_p, right_p):
        rect = self._rect()
        if rect.left < left_p.rect.left or rect.right > right_p.rect.right:
            self.delta = (self.delta[0], -self.delta[1])
        else:
            self.delta = (-self.delta[0], self.delta[1])
        self.click.play()

    def escape_right(self):
        return self.center[0] - self.radius > WIDTH

    def escape_left(self):
        return self.center[0] + self.radius < 0

    def _rect(self):
        half_x = self.radius + abs(self.delta[0])
        half_y = self.radius + abs(self.delta[1])
        return pygame.Rect(self.center[0] - half_x, self.center[1] - half_y,
                2 * half_x, 2 * half_y)


class Board(object):

    def __init__(self):
        self.left_paddle = Paddle(pygame.Rect(10, 200, P_WIDTH, P_HEIGHT), RED)
        self.right_paddle = Paddle(pygame.Rect(780, 200, P_WIDTH, P_HEIGHT), BLUE)
        self.ball = Ball(BALL_START, 9, YELLOW, (7, 4))
        self.left_score = 0
        self.right_score = 0
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.ball.draw()
        self.score_font = pygame.font.SysFont("monospace", 75)
        self.score_margin = 50

    def update(self, keys):
        self._print_score()
        self.ball.move()
        if self.ball.touch_top():
            self.ball.bounce_wall()

        if self.ball.touch_paddle(self.left_paddle, self.right_paddle):
            self.ball.bounce_paddle(self.left_paddle, self.right_paddle)

        if self.ball.escape_right():
            self.left_score += 1
            self._print_score()
            self.ball.delta = -self.ball.delta[0], self.ball.delta[1]
            self.ball.center = BALL_START
        elif self.ball.escape_left():
            self.right_score += 1
            self._print_score()
            self.ball.delta = -self.ball.delta[0], self.ball.delta[1]
            self.ball.center = BALL_START

        if keys[K_a]:
            self.left_paddle.move(-1)
        if keys[K_z]:
            self.left_paddle.move(1)

        if keys[K_UP]:
            self.right_paddle.move(-1)
        if keys[K_DOWN]:
            self.right_paddle.move(1)

        return self.right_score > 2 or self.left_score > 2

    def _print_score(self):
        l_score = self.score_font.render(str(self.left_score), 1, RED)
        r_score = self.score_font.render(str(self.right_score), 1, BLUE)
        margin = self.score_margin
        DISPLAYSURF.fill(BLACK, (margin, margin, WIDTH - 2*margin, 100))
        DISPLAYSURF.blit(l_score, (margin, margin))
        DISPLAYSURF.blit(r_score, (WIDTH - margin - r_score.get_width(), margin))