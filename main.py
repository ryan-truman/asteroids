import pygame
import sys
from constants import *
from player import *
from scoreboard import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!\n" 
          f"Screen width: {SCREEN_WIDTH}\n"  
          f"Screen height: {SCREEN_HEIGHT}"
          )

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    ScoreBoard.containers = (drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    scoreboard = ScoreBoard(SCREEN_WIDTH - 100, 0, 100, 50)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Game Over! Score: {scoreboard.score}")
                raise sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    scoreboard.update_score(1)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
