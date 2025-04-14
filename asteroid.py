import pygame
import random

from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius) 

    def draw(self, screen):
        pygame.draw.circle(screen,"red",self.position, self.radius,2)

    def update(self,dt):
       self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= 3:
            return
        else:
            boom_angle = random.uniform(20,50)
            pt1_velocity = pygame.math.Vector2.rotate(self.velocity, boom_angle)
            pt2_velocity = pygame.math.Vector2.rotate(self.velocity, -boom_angle)
            boom_radius = self.radius - ASTEROID_MIN_RADIUS
            pt1 = Asteroid(self.position.x,self.position.y,boom_radius)
            pt2 = Asteroid(self.position.x,self.position.y,boom_radius)
            pt1.velocity = pt1_velocity
            pt2.velocity = pt2_velocity
