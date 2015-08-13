import pygame
import sys
from pygame.locals import *

from board import board


class Control(object):

    def __init__(self):
        self.board = board
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 50
        self.keys = pygame.key.get_pressed()
        self.states = {}
        self.state = None
        self.state_name = ""

    def setup_states(self, states, start_state):
        self.states = states
        self.state_name = start_state
        self.state = states[start_state]

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.keys)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.states[self.state_name]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
            self.state.get_event(event)

    def main(self):
        """Main loop for entire program"""
        while not self.done:
            self.event_loop()
            self.update()
            pygame.display.update()
            self.clock.tick(self.fps)


def init():
    pygame.init()
    pygame.display.set_caption('Pong FTW!')
    control = Control()
    states = {'welcome': None, 'play': None,
              'game-over': None}
    control.setup_states(states, 'play')
    control.main()

    # while True:
    #     pygame.event.pump()
    #     keys = pygame.key.get_pressed()
    #
    #     board.update()
    #     board.move_paddles(keys)
    #
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     pygame.display.update()


if __name__ == '__main__':
    init()
    pygame.quit()
    sys.exit()
