import math
import random
import pygame
import game.settings as settings
from game.entities.enemy import create_enemy

TILE_SIZE = 32
MAX_ENEMIES = 150

class Spawner:
    def __init__(self):
        self.time = 0.0
        self.timer = 0.0  

    def update(self, dt, session):
        self.time += dt
        self.timer -= dt
        if self.timer <= 0:
            if len(session.world.enemies) < MAX_ENEMIES:
                self._spawn(session)
            self.timer = max(0.5, 2.0 - self.time * 0.02)   

    def _pick_kind(self):
        kinds = ["fox"]
        if self.time > 30:
            kinds.append("wolf")
        if self.time > 60:
            kinds.append("boar")
        if self.time > 120:
            kinds.append("bear")
        return random.choice(kinds)

    def _spawn(self, session):
        # sur un cercle juste en dehors de l'écran, autour du joueur
        radius = pygame.Vector2(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT).length() / 2 + 50
        angle = random.uniform(0, 2 * math.pi)
        position = session.player.position + pygame.Vector2(math.cos(angle), math.sin(angle)) * radius

        # on reste dans la carte
        position.x = max(0, min(position.x, session.world.size[0] * TILE_SIZE))
        position.y = max(0, min(position.y, session.world.size[1] * TILE_SIZE))

        session.world.enemies.append(create_enemy(self._pick_kind(), position))