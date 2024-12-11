import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FPS

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        dt = 0.0
        clock = pygame.time.Clock()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(MAX_FPS)/1000
            
if __name__ == "__main__":
    main()