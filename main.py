import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()

    # Clock for FPS Calc
    clock = pygame.time.Clock()
    dt = 0

    # Set GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers =(updatable)
    Shot.containers = (shot, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2,
                    y = SCREEN_HEIGHT / 2)
    asteroid_filed = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        for sprite in asteroid:
            if sprite.collision(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
