import pygame

HEIGHT = 600
WIDTH = 800
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = 0, 0, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 96
P_HEIGHT = 80
P_WIDTH = 10

pygame.mixer.init()


class Paddle(object):

    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
        self.delta = 10

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def move(self, direction):
        if self.has_room(direction):
            pygame.draw.rect(DISPLAYSURF, BLACK, self.rect)
            self.rect = self.rect.move(0, direction * self.delta)
            pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def has_room(self, direction):
        if direction == 1:
            return HEIGHT - self.delta >= self.rect.bottom
        elif direction == -1:
            return self.delta <= self.rect.top


class Ball(object):

    def __init__(self, center, radius, color, delta):
        self.center = center
        self.radius = radius
        self.color = color
        self.delta = delta
        self.click = pygame.mixer.Sound("../paddle.wav")
        self.bounce = pygame.mixer.Sound("../bounce.wav")

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)

    def move(self):
        pygame.draw.circle(DISPLAYSURF, BLACK, self.center, self.radius)
        self.center = self.center[0] + self.delta[0], self.center[1] + self.delta[1]
        pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)

    def touch_top(self):
        return self.center[1] <= self.radius or self.center[1] >= HEIGHT - self.radius

    def touch_paddle(self, left_p, right_p):
        rect = self._rect()
        return left_p.rect.colliderect(rect) or right_p.rect.colliderect(rect)

    def bounce_wall(self):
        self.delta = (self.delta[0], -self.delta[1])
        self.bounce.play()

    def bounce_paddle(self):
        self.delta = (-self.delta[0], self.delta[1])
        self.click.play()

    def escape_right(self):
        return self.center[0] - self.radius > WIDTH

    def escape_left(self):
        return self.center[0] + self.radius < 0

    def _rect(self):
        half_x = self.radius + abs(self.delta[0])
        half_y = self.radius + abs(self.delta[1])
        return (self.center[0] - half_x, self.center[1] - half_y,
                2 * half_x, 2 * half_y)
