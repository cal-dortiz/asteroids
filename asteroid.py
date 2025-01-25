import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, 
                            color='white', 
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0,50.0)
            random_angle = self.velocity.rotate(angle)
            neg_random_angle = self.velocity.rotate(-1*angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            astroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
            astroid_2 = Asteroid(self.position.x, self.position.y,new_radius)

            astroid_1.velocity = random_angle*1.2
            astroid_2.velocity = neg_random_angle*1.2

