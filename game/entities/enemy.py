# game/entities/enemy.py
import pygame
from game.entities.entity import Entity
from game.entities.entity_type import EntityType

ANIMALS = {
    "fox":  {"health": 8,   "attack": 6,  "move_speed": 125, "xp_reward": 12},
    "wolf": {"health": 18,  "attack": 11, "move_speed": 95,  "xp_reward": 18},
    "boar": {"health": 40,  "attack": 15, "move_speed": 75,  "xp_reward": 30},
    "bear": {"health": 95,  "attack": 22, "move_speed": 55,  "xp_reward": 60},
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
        self.direction = 1
        self.frame = 0        

    def update(self, dt, target):
        self.attack_timer -= dt

        to_target = target.position - self.position
        dist = to_target.length()

        if dist > self.contact_range:
            if abs(to_target.x) > abs(to_target.y):
                self.direction = 3 if to_target.x > 0 else 2
            else:
                self.direction = 1 if to_target.y > 0 else 0

            self.position += to_target / dist * self.move_speed * dt

        elif self.attack_timer <= 0:
            damage = target.take_damage(self.attack)

            if damage > 0 and target.entity_type == EntityType.PLAYER:
                target.damage_received = True

            self.attack_timer = self.attack_cooldown

def create_enemy(kind, position):
        return Enemy(kind, position, **ANIMALS[kind])