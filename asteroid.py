import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, self.radius)

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self,asteroidfield):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        split_asteroid_velocity1 = self.velocity.rotate(random_angle)
        split_asteroid_velocity2 = self.velocity.rotate(-random_angle)
        split_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroidfield.spawn(split_asteroids_radius, self.position, (split_asteroid_velocity1 * 1.2))
        asteroidfield.spawn(split_asteroids_radius, self.position, (split_asteroid_velocity2 * 1.2))


        
