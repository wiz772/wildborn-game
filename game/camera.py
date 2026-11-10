import pygame
import settings

class Camera:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0,0)

    def update(self, target_position):
        player_center = target_position + pygame.Vector2(16, 16)

        self.position = player_center - pygame.Vector2(
            settings.SCREEN_WIDTH // 2,
            settings.SCREEN_HEIGHT // 2
        )