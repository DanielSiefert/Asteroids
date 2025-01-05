import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2
    dt = 0.0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(x, y)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)

    AsteroidField.containers = (updateable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for p in drawable:
            p.draw(screen)
        for p in updateable:
            p.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()
        for a in asteroids:
            for shot in shots:
                if a.collision(shot):
                    shot.kill()
                    a.split(asteroidfield)
        pygame.display.flip()
        dt = ((clock.tick(60)) / 1000)

if __name__ == "__main__":
    main()