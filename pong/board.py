import pygame

HEIGHT = 600
WIDTH = 800
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = 0, 0, 0


paddle_delta = 10

class Paddle(object):

    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def move(self, direction):
        pygame.draw.rect(DISPLAYSURF, BLACK, self.rect)
        self.rect = self.rect.move(0, direction * paddle_delta)
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect)
