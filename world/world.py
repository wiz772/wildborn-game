import world.generation.generate as generate
import world.perlin_noise as perlin_noise

class World:
    def __init__(self, size: tuple[int, int], frequency: float, seed: int | None = None):
        self.size = size
        self.frequency = frequency
        self.terrains = []
        self.objects = []
        self.animals = []
        self.noise = perlin_noise.PerlinNoise(size[0], size[1], seed)
        self.seed = self.noise.seed

    def generate_random_world(self):
        self.terrains = generate.generate_terrain(self.size, self.noise, self.frequency)
        self.objects = generate.generate_objects(self.size, self.noise, self.frequency)
        