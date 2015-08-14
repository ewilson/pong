import pygame
from pygame.locals import *

from board import DISPLAYSURF, Board, Paddle, Ball, WIDTH, P_HEIGHT, P_WIDTH
from board import RED, BLUE, YELLOW


class Play(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'game-over'
        self.board = None

    def update(self, keys):
        print 'Play'
        if not self.board:
            self.board = Board(Paddle(pygame.Rect(10, 200, P_WIDTH, P_HEIGHT), RED),
                               Paddle(pygame.Rect(780, 200, P_WIDTH, P_HEIGHT), BLUE))
        self.done = self.board.update(keys)
        if self.done:
            self.board = None

    def cleanup(self):
        self.board = None
        self.done = False
        # paddle cleanup needed


class Welcome(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'play'

    def update(self, keys):
        print 'Welcome'
        if keys[K_SPACE]:
            self.done = True

    def cleanup(self):
        self.done = False


class GameOver(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'play'

    def update(self, keys):
        print 'GO'
        if keys[K_SPACE]:
            self.done = True

    def cleanup(self):
        self.done = False
