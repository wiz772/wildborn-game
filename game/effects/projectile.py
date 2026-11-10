
import pygame

PROJECTILE_LIFETIME = 2.0
PROJECTILE_SPEED = 350
PROJECTILE_RADIUS = 5

class Projectile:
    def __init__(self, position, target, damage):
        self.position = pygame.Vector2(position) + pygame.Vector2(16, 16)
        self.direction = pygame.Vector2(target.position) + pygame.Vector2(16, 16) - self.position

        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()

        self.damage = damage
        self.speed = PROJECTILE_SPEED
        self.radius = PROJECTILE_RADIUS

        self.lifetime = PROJECTILE_LIFETIME
        self.active = True

    def update(self, dt, enemies):
        if not self.active:
            return

        self.lifetime -= dt

        if self.lifetime <= 0:
            self.active = False
            return

        self.position += self.direction * self.speed * dt

        for enemy in enemies:
            if not enemy.is_alive():
                continue

            enemy_center = enemy.position + pygame.Vector2(16, 16)

            if self.position.distance_to(enemy_center) <= self.radius + 12:
                enemy.take_damage(self.damage)
                self.active = False
                break

    def draw(self, screen, camera):
        if not self.active:
            return

        screen_position = self.position - camera.position

        pygame.draw.circle(
            screen,
            (230, 190, 80),
            (round(screen_position.x), round(screen_position.y)),
            self.radius
        )
