import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FPS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    my_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    my_asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(clock.tick(MAX_FPS)/1000)
            
if __name__ == "__main__":
    main()