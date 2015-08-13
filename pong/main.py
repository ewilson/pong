import pygame
import sys
from pygame.locals import *

from board import board, BALL_START

pygame.init()
fps_clock = pygame.time.Clock()
pygame.display.set_caption('Pong FTW!')

TOC = 50

left_score = 0
right_score = 0

while True:
    result = board.update()
    if result == 'LEFT_SCORE':
        left_score += 1
        board.ball.delta = -board.ball.delta[0], board.ball.delta[1]
        board.ball.center = BALL_START

    if result == 'RIGHT_SCORE':
        right_score += 1
        board.ball.delta = -board.ball.delta[0], board.ball.delta[1]
        board.ball.center = BALL_START

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    board.move_paddles(keys)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fps_clock.tick(TOC)
