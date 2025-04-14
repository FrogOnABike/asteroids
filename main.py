# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_timer = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    craft = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    astro_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        #Player collision detetion
        for roid in asteroids:
            if roid.collision(craft):
                print("Game Over!")
                sys.exit()

        for roid in asteroids:
            for pew in shots:
                if pew.collision(roid):
                    roid.kill()
                    pew.kill()

        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()
        dt = screen_timer.tick(60)/1000
        screen_timer.tick(60)

if __name__ == "__main__":
    main()