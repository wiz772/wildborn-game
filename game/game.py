import pygame
import game.settings as settings
class Game:
    def __init__(self):
        screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_NAME)

        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                
            pygame.display.flip()
            clock.tick(settings.FPS)