from dataclasses import dataclass
from game.world.world import World
from game.entities.player import Player
from game.camera import Camera
from game.entities.enemy_spawner import Spawner

@dataclass
class Session:
    world: World
    player: Player
    spawner: Spawner
    camera: Camera
    elapsed_time : float