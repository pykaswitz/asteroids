import pygame
import circleshape
from shot import Shot
import constants

class Player (circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class / A player will look like a triangle, even though we'll use a circle to represent its hitbox
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):        
        attack = Shot(self.position, constants.SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        attack.velocity = forward * constants.PLAYER_SHOOT_SPEED
        self.timer = constants.PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
            
        if keys[pygame.K_d]:
            self.rotate(dt * 1)

        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_w]:
            self.move(dt * 1)

        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                pass
            else:
                self.shoot()
