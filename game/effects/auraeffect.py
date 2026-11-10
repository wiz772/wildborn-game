import pygame


class AuraEffect:
    def __init__(self, weapon):
        self.weapon = weapon
        self.pulsing = False
        self.current_size = 0
        self.pulse_speed = 300

    def pulse(self):
        self.current_size = self.weapon.area_size
        self.pulsing = True

    def update(self, dt):
        if self.pulsing:
            self.current_size += self.pulse_speed * dt

            if self.current_size >= self.weapon.area_size * 1.2:
                self.current_size = 0
                self.pulsing = False

    def draw(self, screen, camera, player):
        player_center = player.position + pygame.Vector2(16, 16)
        position = player_center - camera.position + camera.shake_offset

        size = self.current_size if self.pulsing else self.weapon.area_size

        pygame.draw.circle(
            screen,
            (100, 200, 255),
            (int(position.x), int(position.y)),
            int(size),
            2
        )

    def is_alive(self):
        return True