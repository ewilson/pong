import pygame
from pygame.locals import *

from board import DISPLAYSURF


class Welcome(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'game-over'

    def update(self, keys):
        if keys[K_UP]:
            pygame.draw.circle(DISPLAYSURF, (0,0,00), (200, 400), 25)
            pygame.draw.circle(DISPLAYSURF, (100,200,50), (200, 200), 25)
        if keys[K_DOWN]:
            pygame.draw.circle(DISPLAYSURF, (0,0,0), (200, 200), 25)
            pygame.draw.circle(DISPLAYSURF, (100,200,50), (200, 400), 25)
        if keys[K_SPACE]:
            pygame.draw.circle(DISPLAYSURF, (100,200,50), (400, 300), 50)
            self.done = True


class GameOver(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'welcome'

    def update(self, keys):
        if keys[K_SPACE]:
            pygame.draw.circle(DISPLAYSURF, (50,100,200), (400, 300), 50)
            self.done = True
