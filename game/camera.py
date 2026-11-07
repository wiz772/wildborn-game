import pygame
import game.settings

class Camera:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0,0)

    def update(self, target_position):
        player_center = target_position + pygame.Vector2(16, 16)

        self.position = player_center - pygame.Vector2(
            game.settings.SCREEN_WIDTH // 2,
            game.settings.SCREEN_HEIGHT // 2

        )