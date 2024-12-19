import pygame
from player import Player
from constants import *

def main():
    pygame.init()

    # Clock for FPS Calc
    clock = pygame.time.Clock()
    dt = 0

    # Set GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiat Player
    player = Player(x = SCREEN_WIDTH / 2,
                    y = SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    # print("Starting asteroids!")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
