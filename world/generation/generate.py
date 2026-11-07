from world.perlin_noise import PerlinNoise
from .rules import get_terrain
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

def generate_trees(terrain, seed, density=0.6):
    rng = random.Random(seed + 1)
    trees = []
    for x, row in enumerate(terrain):
        for y, terrain in enumerate(row):
            if terrain == "grass" and rng.random() < density:
                trees.append((x, y))
    return trees
