import pygame
import sys
from pygame.locals import *

from board import board


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Pong FTW!')

    TOC = 50

    while True:
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        board.update()
        board.move_paddles(keys)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fps_clock.tick(TOC)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()