import pygame
from constants import *

def main():
    pygame.init()

    # Clock for FPS Calc
    clock = pygame.time.Clock()
    dt = 0

    # Set GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    # print("Starting asteroids!")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
