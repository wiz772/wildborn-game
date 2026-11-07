from dataclasses import dataclass
from world.world import World
from game.entities.player import Player
from game.camera import Camera

@dataclass
class Session:
    world: World
    player: Player
    camera: Camera