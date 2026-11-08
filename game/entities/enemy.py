# game/entities/enemy.py
import pygame
from game.entities.entity import Entity
from game.entities.entity_type import EntityType

ANIMALS = {
    "fox":  {"health": 6,  "attack": 7,  "move_speed": 110, "xp_reward": 3},
    "wolf": {"health": 12, "attack": 9,  "move_speed": 85,  "xp_reward": 6},
    "boar": {"health": 25, "attack": 10, "move_speed": 70,  "xp_reward": 10},
    "bear": {"health": 60, "attack": 14, "move_speed": 50,  "xp_reward": 25},
}

class Enemy(Entity):
    def __init__(self, kind, position, health, attack, move_speed, xp_reward):
        super().__init__(health, health, 0, attack, move_speed, EntityType.MONSTER)
        self.kind = kind                      # "fox", "wolf"... sert à choisir le sprite
        self.position = pygame.Vector2(position)
        self.xp_reward = xp_reward
        self.contact_range = 24
        self.attack_cooldown = 1.0
        self.attack_timer = 0.0                           

    def update(self, dt, target):
        self.attack_timer -= dt
        to_target = target.position - self.position
        dist = to_target.length()
        if dist > self.contact_range:
            self.position += to_target / dist * self.move_speed * dt
        elif self.attack_timer <= 0:
            target.take_damage(self.attack)
            self.attack_timer = self.attack_cooldown

def create_enemy(kind, position):
    return Enemy(kind, position, **ANIMALS[kind])