from game.entities.entity import Entity
from game.entities.entity_type import EntityType
import game.settings
import pygame

DEFAULT_HEALTH = 10
DEFAULT_MAX_HEALTH = 10
DEFAULT_DEFENSE = 5
DEFAULT_ATTACK = 5
DEFAULT_MOVE_SPEED_PIXEL = 150

class Player(Entity):
    def __init__(self, game_instance):
        super().__init__(DEFAULT_HEALTH, DEFAULT_MAX_HEALTH, DEFAULT_DEFENSE, DEFAULT_ATTACK, DEFAULT_MOVE_SPEED_PIXEL, EntityType.PLAYER)
        self.position = pygame.Vector2(game.settings.WORLD_SIZE[0] * 32 // 2, game.settings.WORLD_SIZE[1] * 32 // 2)
        self.upgrades = []
        self.totems = []

    def update(self, direction, dt):
        if direction is None:
            raise ValueError("Player.update() direction is null")

        if direction.length() > 0:
            direction = direction.normalize()

        velocity = direction * self.move_speed
        self.position += velocity * dt