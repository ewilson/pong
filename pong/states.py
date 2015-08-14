import pygame
from pygame.locals import *

from board import Board, DISPLAYSURF, HEIGHT, WIDTH, BLACK


class Play(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'game-over'
        self.board = None

    def update(self, keys):
        if not self.board:
            self.board = Board()
        self.done = self.board.update(keys)

    def cleanup(self):
        self.board.left_paddle.cleanup()
        self.board.right_paddle.cleanup()
        self.board = None
        self.done = False


class Welcome(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.ready = False
        self.next = 'play'
        self.font_size = 1
        self.normal_font = pygame.font.SysFont("monospace", 15)

    def update(self, keys):
        if self.font_size <= 200:
            welcome = pygame.font.SysFont("monospace", self.font_size)
            pong = welcome.render("PONG!", 1, (0,255,0))
            w = pong.get_width()
            h = pong.get_height()
            x = (WIDTH - w) / 2
            y = (HEIGHT - h) / 2
            DISPLAYSURF.fill(BLACK, (x, y, w, h))
            DISPLAYSURF.blit(pong, (x,y))
            self.font_size += 1
        elif not self.ready:
            begin = self.normal_font.render("Press space bar to start", 1, (0,255,0))
            DISPLAYSURF.blit(begin, ((WIDTH - begin.get_width()) / 2, 400))
            self.ready = True
        if keys[K_SPACE]:
            self.done = True

    def cleanup(self):
        self.done = False
        DISPLAYSURF.fill(BLACK)


class GameOver(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'play'

    def update(self, keys):
        if keys[K_SPACE]:
            self.done = True

    def cleanup(self):
        self.done = False
