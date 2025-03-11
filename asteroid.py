from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width=2)
    
    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        A1_vector = pygame.math.Vector2.rotate(self.velocity, random_angle)
        A2_vector = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        A1 = Asteroid(self.position.x, self.position.y, new_radius)
        A2 = Asteroid(self.position.x, self.position.y, new_radius)
        A1.velocity = A1_vector * 1.2
        A2.velocity = A2_vector * 1.2

