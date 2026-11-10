
import pygame

class ClawEffect:
    def __init__(self, player_position, target_position):
        self.start = pygame.Vector2(player_position) + pygame.Vector2(16, 16)
        self.target = pygame.Vector2(target_position) + pygame.Vector2(16, 16)

        self.timer = 0.12
        self.duration = 0.12

    def update(self, dt):
        self.timer -= dt

    def is_alive(self):
        return self.timer > 0

    def draw(self, screen, camera):
        direction = self.target - self.start

        if direction.length_squared() == 0:
            return

        direction = direction.normalize()
        perpendicular = pygame.Vector2(-direction.y, direction.x)

        center = self.target - direction * 12
        alpha = max(0, self.timer / self.duration)

        for offset in [-5, 0, 5]:
            start = center + perpendicular * offset - direction * 8
            end = center + perpendicular * offset + direction * 8

            start -= camera.position
            end -= camera.position

            pygame.draw.line(
                screen,
                (255, 240, 220),
                start,
                end,
                2
            )
