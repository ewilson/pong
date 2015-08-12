import pygame
import sys
from pygame.locals import *

from board import Paddle
from board import DISPLAYSURF, HEIGHT, WIDTH


pygame.init()

fps_clock = pygame.time.Clock()

pygame.display.set_caption('Pong FTW!')
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 96
BLACK = 0, 0, 0

left_paddle = Paddle(pygame.Rect(10, 200, 10, 80), RED)
right_paddle = Paddle(pygame.Rect(780, 0, 10, 80), BLUE)
ball_center = 40, 50
BALL_RADIUS = 9

left_paddle.draw()
right_paddle.draw()
pygame.draw.circle(DISPLAYSURF, YELLOW, ball_center, BALL_RADIUS)

ball_x_delta = 7
ball_y_delta = 4
paddle_delta = 10
TOC = 50


def touch_top():
    return ball_center[1] <= BALL_RADIUS or ball_center[1] >= HEIGHT - BALL_RADIUS


def touch_paddle():
    ball_rect = ball_center[0] - BALL_RADIUS, ball_center[1] - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS
    return left_paddle.rect.colliderect(ball_rect) or right_paddle.rect.colliderect(ball_rect)


def move_ball():
    new_ball_center = ball_center[0] + ball_x_delta, ball_center[1] + ball_y_delta
    pygame.draw.circle(DISPLAYSURF, BLACK, ball_center, BALL_RADIUS)
    pygame.draw.circle(DISPLAYSURF, YELLOW, new_ball_center, BALL_RADIUS)
    return new_ball_center


def has_room_above(paddle):
    return paddle.top - paddle_delta >= 0


def has_room_below(paddle):
    return paddle.bottom + paddle_delta <= HEIGHT


while True:
    if touch_top():
        ball_y_delta = -ball_y_delta

    if touch_paddle():
        ball_x_delta = -ball_x_delta

    ball_center = move_ball()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_a] and has_room_above(left_paddle.rect):
        left_paddle.move(-1)
    if keys[K_z] and has_room_below(left_paddle.rect):
        left_paddle.move(1)

    right_delta = 0
    if keys[K_UP] and has_room_above(right_paddle.rect):
        right_paddle.move(-1)
    if keys[K_DOWN] and has_room_below(right_paddle.rect):
        right_paddle.move(1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(TOC)
