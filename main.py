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

    while True:
        for event in pyg.event.get():       #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pyg.QUIT:
                return
        screen.fill((0,0,0))
        pyg.display.flip()


if __name__ == "__main__":
    main()
