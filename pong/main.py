import pygame
import sys
from pygame.locals import *

from board import Paddle, Ball, RED, BLUE, YELLOW, P_HEIGHT, P_WIDTH


pygame.init()

fps_clock = pygame.time.Clock()

pygame.display.set_caption('Pong FTW!')

left_paddle = Paddle(pygame.Rect(10, 200, P_WIDTH, P_HEIGHT), RED)
right_paddle = Paddle(pygame.Rect(780, 200, P_WIDTH, P_HEIGHT), BLUE)
ball = Ball((40, 50), 9, YELLOW, (7, 4))

left_paddle.draw()
right_paddle.draw()
ball.draw()

TOC = 50

while True:
    if ball.touch_top():
        ball.bounce_wall()

    if ball.touch_paddle(left_paddle, right_paddle):
        ball.bounce_paddle()

    ball.move()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        left_paddle.move(-1)
    if keys[K_z]:
        left_paddle.move(1)

    right_delta = 0
    if keys[K_UP]:
        right_paddle.move(-1)
    if keys[K_DOWN]:
        right_paddle.move(1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(TOC)
