# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player
from asteroids import Asteroid
import asteroidfield
from circleshape import CircleShape
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # Use pygame's display.set_mode() to get a new GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2

    # Asteroid container
    asteroid_g = pygame.sprite.Group()
    # Player container
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_g, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    my_player = player.Player(x, y)
    my_asteroid_field = asteroidfield.AsteroidField()

    
    while True:
        for event in pygame.event.get():
            # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        # creates a window using screen obj and fills it solid black
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # sets screen refresh to 60fps and updates dt (delta time) from miliseconds to seconds
        updatable.update(dt)
        for a in asteroid_g:
            if my_player.collision(a):
                print("Game over!")
                sys.exit()


if __name__ == "__main__":
    main()
