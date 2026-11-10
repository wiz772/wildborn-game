import pygame
import settings
import random

class Camera:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0,0)
        self.shake_duration = 0
        self.shake_intensity = 0
        self.shake_offset = pygame.Vector2()

    def update(self, target_position):
        player_center = target_position + pygame.Vector2(16, 16)

        self.position = player_center - pygame.Vector2(
            settings.SCREEN_WIDTH // 2,
            settings.SCREEN_HEIGHT // 2
        )

    def shake(self, intensity=8, duration=0.2):
        self.shake_intensity = intensity
        self.shake_duration = duration

    def update_shake(self, dt):
        if self.shake_duration > 0:
            self.shake_duration -= dt

            self.shake_offset.x = random.uniform(
                -self.shake_intensity,
                self.shake_intensity
            )
            self.shake_offset.y = random.uniform(
                -self.shake_intensity,
                self.shake_intensity
            )
        else:
            self.shake_offset = pygame.Vector2()