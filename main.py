import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FPS
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        my_player.draw(screen)
        dt = 0.0
        clock = pygame.time.Clock()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(MAX_FPS)/1000
            
if __name__ == "__main__":
    main()