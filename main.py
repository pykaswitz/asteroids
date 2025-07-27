# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame as pyg
import constants as cons

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {cons.SCREEN_WIDTH}")
    print(f"Screen height: {cons.SCREEN_HEIGHT}")

    # Use pygame's display.set_mode() to get a new GUI window
    screen = pyg.display.set_mode((cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT))
    clock = pyg.time.Clock()
    dt = 0

    while True:
        for event in pyg.event.get():       # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pyg.QUIT:
                return
        screen.fill((0,0,0))                # creates a window using screen obj and fills it solid black
        pyg.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000          # sets screen refresh to 60fps and updates dt (delta time) from miliseconds to seconds


if __name__ == "__main__":
    main()
