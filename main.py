import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    while(1):
        """ This will make the windows close button work. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Asteroids...")
                return
        screen.fill(color="black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
