import pygame

# Base class for game objects
class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.rect = (x, y, width, height)
        self.text_position = (x + 5, height/3)
        self.score = 0
        self.text_surface = pygame.font.Font(None, size=30).render(str(f"Score:{self.score}"), True, "white")


    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, 2)
        screen.blit(self.text_surface, self.text_position)
    
    def update_score(self, points):
        """Updates the score and re-renders the text."""
        self.score += points
        self.text_surface = pygame.font.Font(None, size=30).render(str(self.score), True, "white")
        