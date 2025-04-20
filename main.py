import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!\n" 
          f"Screen width: {SCREEN_WIDTH}\n"  
          f"Screen height: {SCREEN_HEIGHT}"
          )
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
    
        
        clock.tick(60)  # Limit to 60 FPS
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        

if __name__ == "__main__":
    main()
