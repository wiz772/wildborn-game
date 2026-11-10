import game.world.generation.generate as generate
import game.world.perlin_noise as perlin_noise

class World:
    def __init__(self, size: tuple[int, int], frequency: float, seed: int | None = None):
        self.size = size
        self.frequency = frequency

        self.terrain_noise = perlin_noise.PerlinNoise(10, 10, seed)
        self.seed = self.terrain_noise.seed

        # self.rock_noise = perlin_noise.PerlinNoise(size[0], size[1], self.seed + 1)
        # self.vegetation_noise = perlin_noise.PerlinNoise(size[0], size[1], self.seed + 2)

        self.terrains = []
        self.objects = []
        self.enemies = []

        self.effects = []
        self.projectiles = []

    def generate_random_world(self):
        self.terrains = generate.generate_terrain(generate.generate_noise_map(self.size, self.terrain_noise, self.frequency))
        self.objects += generate.generate_trees(self.terrains, self.seed, 0.3)
        