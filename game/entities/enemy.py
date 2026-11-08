from game.entities.entity import Entity
from game.entities.entity_type import EntityType
import game.settings
import pygame

class Enemy(Entity):
    def __init__(self, position, health=10, attack=8, move_speed=70):
        super().__init__(health, health, 0, attack, move_speed, EntityType.MONSTER)
        self.position = pygame.Vector2(position)
        self.contact_range = 24
        self.attack_cooldown = 1.0
        self.attack_timer = 0.0
        self.xp_reward = 5 

    def update(self, dt, target):
        self.attack_timer -= dt
        to_target = target.position - self.position
        dist = to_target.length()
        if dist > self.contact_range:
            self.position += to_target / dist * self.move_speed * dt
        elif self.attack_timer <= 0:
            target.take_damage(self.attack)
            self.attack_timer = self.attack_cooldown