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
right_paddle = pygame.Rect(780, 200, 10, 75)
ball_center = 40, 50
BALL_RADIUS = 9

pygame.draw.rect(DISPLAYSURF, RED, left_paddle)
pygame.draw.rect(DISPLAYSURF, BLUE, right_paddle)
pygame.draw.circle(DISPLAYSURF, YELLOW, ball_center, BALL_RADIUS)

ball_x_delta = 2
ball_y_delta = 1
while True:
    if ball_center[0] <= BALL_RADIUS or ball_center[0] >= WIDTH - BALL_RADIUS:
        ball_x_delta = -ball_x_delta
    if ball_center[1] <= BALL_RADIUS or ball_center[1] >= HEIGHT - BALL_RADIUS:
        ball_y_delta = -ball_y_delta

    new_ball_center = ball_center[0] + ball_x_delta, ball_center[1] + ball_y_delta
    pygame.draw.circle(DISPLAYSURF, BLACK, ball_center, BALL_RADIUS)
    pygame.draw.circle(DISPLAYSURF, YELLOW, new_ball_center, BALL_RADIUS)
    ball_center = new_ball_center

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(150)
