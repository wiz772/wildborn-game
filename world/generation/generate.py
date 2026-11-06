from world.perlin_noise import PerlinNoise
from .rules import get_terrain

def generate_terrain(size: tuple[int, int], noise:PerlinNoise, frequency):
    terrains = []

    for y in range(size[1]):
        row = []

        for x in range(size[0]):
            value = noise.get_noise(x * frequency, y * frequency)
            row.append(get_terrain(value))

        terrains.append(row)

    return terrains 

def generate_objects(size: tuple[int, int], noise:PerlinNoise, frequency):
    ...