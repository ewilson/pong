from pygame.locals import *

from board import Board


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
        self.next = 'play'

    def update(self, keys):
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
        if keys[K_SPACE]:
            self.done = True

    def cleanup(self):
        self.done = False
