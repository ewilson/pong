from pygame.locals import *


class Welcome(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'game-over'
        print 'Welcome'

    def update(self, keys):
        if keys[K_SPACE]:
            self.done = True


class GameOver(object):

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = 'welcome'
        print 'Game OVer?'

    def update(self, keys):
        if keys[K_SPACE]:
            self.done = True