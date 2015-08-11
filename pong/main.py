import pygame, sys
from pygame.locals import *

pygame.init()

fps_clock = pygame.time.Clock()

HEIGHT = 600
WIDTH = 800
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong FTW!')
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 96
BLACK = 0, 0, 0

left_paddle = pygame.Rect(10, 200, 10, 75)
right_paddle = pygame.Rect(780, 0, 10, 600)
ball_center = 40, 50
BALL_RADIUS = 9

pygame.draw.rect(DISPLAYSURF, RED, left_paddle)
pygame.draw.rect(DISPLAYSURF, BLUE, right_paddle)
pygame.draw.circle(DISPLAYSURF, YELLOW, ball_center, BALL_RADIUS)

ball_x_delta = 7
ball_y_delta = 4
TOC = 50

def touch_top(ball_center):
    if ball_center[1] <= BALL_RADIUS or ball_center[1] >= HEIGHT - BALL_RADIUS:
        return True


def touch_paddle(ball_center, left_paddle, right_paddle):
    ball_rect = ball_center[0] - BALL_RADIUS, ball_center[1] - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS
    return left_paddle.colliderect(ball_rect) or right_paddle.colliderect(ball_rect)

while True:
    if touch_top(ball_center):
        ball_y_delta = -ball_y_delta

    if touch_paddle(ball_center, left_paddle, right_paddle):
        ball_x_delta = -ball_x_delta

    new_ball_center = ball_center[0] + ball_x_delta, ball_center[1] + ball_y_delta
    pygame.draw.circle(DISPLAYSURF, BLACK, ball_center, BALL_RADIUS)
    pygame.draw.circle(DISPLAYSURF, YELLOW, new_ball_center, BALL_RADIUS)
    ball_center = new_ball_center

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        new_lp = left_paddle.move(0, -5)
        pygame.draw.rect(DISPLAYSURF, BLACK, left_paddle)
        pygame.draw.rect(DISPLAYSURF, RED, new_lp)
        left_paddle = new_lp
    elif keys[K_z]:
        new_lp = left_paddle.move(0, 5)
        pygame.draw.rect(DISPLAYSURF, BLACK, left_paddle)
        pygame.draw.rect(DISPLAYSURF, RED, new_lp)
        left_paddle = new_lp

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(TOC)
