import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while(1):
        """ This will make the windows close button work. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Asteroids...")
                return
        screen.fill(color="black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
