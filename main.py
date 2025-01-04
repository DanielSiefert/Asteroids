import pygame
from constants import *
from player import *

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
    player = Player(x, y)
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    drawable.add(PLayer)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = ((clock.tick(60)) / 1000)
if __name__ == "__main__":
    main()