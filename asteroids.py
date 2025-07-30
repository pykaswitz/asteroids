import pygame
import circleshape

class Asteroid (circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(pygame.sprite.Sprite)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.x, self.y, self.radius, width=2)

    def update(self):
        