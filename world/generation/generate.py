from world.perlin_noise import PerlinNoise
from .rules import get_terrain
from world.world_object import WorldObject
import random

def generate_noise_map(size: tuple[int, int], noise:PerlinNoise, frequency, scale=1):
    values = []

    for y in range(size[1]):
        row = []

        for x in range(size[0]):
            noise_x = (x / size[0]) * noise.width * frequency
            noise_y = (y / size[1]) * noise.height * frequency

            value = noise.get_noise(noise_x, noise_y)
            row.append(value)

        values.append(row)

    return values 

def generate_terrain(noise_map):
    return [
        [get_terrain(value) for value in row]
        for row in noise_map
    ]

def generate_trees(terrains, seed, density=0.06):
    rng = random.Random(seed + 1)
    trees = []
    for y, row in enumerate(terrains):
        for x, tile in enumerate(row):          
            if tile == "grass" and rng.random() < density:
                trees.append(WorldObject(x, y, "tree", rng.randrange(3)))
    return trees

