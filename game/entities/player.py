from game.entities.entity import Entity
from game.entities.entity_type import EntityType
import settings
import pygame
from game.weapons.claws import Claws

DEFAULT_HEALTH = 10
DEFAULT_MAX_HEALTH = 10
DEFAULT_DEFENSE = 5
DEFAULT_ATTACK = 5
DEFAULT_MOVE_SPEED_PIXEL = 150

class Player(Entity):
    def __init__(self):
        super().__init__(DEFAULT_HEALTH, DEFAULT_MAX_HEALTH, DEFAULT_DEFENSE, DEFAULT_ATTACK, DEFAULT_MOVE_SPEED_PIXEL, EntityType.PLAYER)
        self.position = pygame.Vector2(settings.WORLD_SIZE[0] * 32 // 2, settings.WORLD_SIZE[1] * 32 // 2)
        self.upgrades = []
        self.totems = []
        self.weapons = [Claws()]
        self.damage_received = False

        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 10

        self.pending_upgrade = 0
        self.choices = []

        self.direction = 1
        self.frame = 0      

    def update(self, direction, dt):
        if direction is None:
            raise ValueError("Player.update() direction is null")

        if direction.length() > 0:
            if abs(direction.x) > abs(direction.y):
                self.direction = 3 if direction.x > 0 else 2
            else:
                self.direction = 1 if direction.y > 0 else 0

            direction = direction.normalize()

        velocity = direction * self.move_speed
        self.position += velocity * dt

        world_width = settings.WORLD_SIZE[0] * 32
        world_height = settings.WORLD_SIZE[1] * 32

        self.position.x = max(0, min(self.position.x, world_width - 32))
        self.position.y = max(0, min(self.position.y, world_height - 32))

    def level_up(self):
        self.level += 1
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.pending_upgrade += 1

    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()