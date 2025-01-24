import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
       self.SHOT_RADIUS = 5
       super().__init__(x, y, self.SHOT_RADIUS)
       self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(surface=screen, 
                            color='white', 
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self, dt):
        self.position += self.velocity * dt
