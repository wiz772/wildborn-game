import math
import random

class PerlinNoise:
    def __init__(self, width: int, height: int, seed: int | None = None):
        if type(width) is not int or type(height) is not int:
            raise TypeError("width and height should only be integers")

        if width <= 0 or height <= 0:
            raise ValueError("width and height should be positive integers")

        self.width = width
        self.height = height

        self.seed = seed if seed is not None else random.randint(0, 2**32 - 1)
        self.rng = random.Random(self.seed)

        self.gradients = self._create_gradients_matrice(self.width, self.height)
    
    def _generate_random_angle(self) -> float:
        return self.rng.uniform(0, 2*math.pi)

    def _create_gradients_matrice(self, width: int, height: int) -> list: 
        matrice = []
        columns = width + 1
        rows = height + 1

        for y in range(rows):
            row_list = []
            for x in range(columns):
                angle = self._generate_random_angle()

                gx = math.cos(angle)
                gy = math.sin(angle)
                gradient = (gx, gy)

                row_list.append(gradient)

            matrice.append(row_list)
        return matrice

    def _calculate_vectors(self, x: float, y: float) -> tuple:
        cell_x = math.floor(x)
        cell_y = math.floor(y)

        top_left_corner_x, top_left_corner_y = (cell_x, cell_y)
        top_right_corner_x, top_right_corner_y = (cell_x + 1, cell_y)
        bottom_left_corner_x, bottom_left_corner_y = (cell_x, cell_y + 1)
        bottom_right_corner_x, bottom_right_corner_y = (cell_x + 1, cell_y + 1)

        top_left_vector = (x - top_left_corner_x, y - top_left_corner_y)
        top_right_vector = (x - top_right_corner_x, y - top_right_corner_y)
        bottom_left_vector = (x - bottom_left_corner_x, y - bottom_left_corner_y)
        bottom_right_vector = (x - bottom_right_corner_x, y - bottom_right_corner_y)

        return (top_left_vector, top_right_vector, bottom_left_vector, bottom_right_vector)

    def _dot_product(self, vector_a: tuple, vector_b: tuple) -> float:
        return (vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1])

    def _get_all_dot_products(self, x: float, y: float) -> tuple:
        cell_x = math.floor(x)
        cell_y = math.floor(y)
        top_left_vector, top_right_vector, bottom_left_vector, bottom_right_vector = self._calculate_vectors(x, y)
        top_left_gradient, top_right_gradient, bottom_left_gradient, bottom_right_gradient = self.gradients[cell_y][cell_x], self.gradients[cell_y][cell_x + 1], self.gradients[cell_y + 1][cell_x], self.gradients[cell_y + 1][cell_x + 1]

        top_left_dot_product = self._dot_product(top_left_vector, top_left_gradient)
        top_right_dot_product = self._dot_product(top_right_vector, top_right_gradient)
        bottom_left_dot_product = self._dot_product(bottom_left_vector, bottom_left_gradient)
        bottom_right_dot_product = self._dot_product(bottom_right_vector, bottom_right_gradient)

        return (top_left_dot_product, top_right_dot_product, bottom_left_dot_product, bottom_right_dot_product)

    def _fade(self, t: float) -> float:
        return t**3 * (t * (6*t - 15) + 10)

    def _lerp(self, a:float, b:float, t:float) -> float:
        return a + t * (b - a)

    def _interpolate_dot_products(self, x: float, y: float) -> float:
        top_left_dot_product, top_right_dot_product, bottom_left_dot_product, bottom_right_dot_product = self._get_all_dot_products(x, y)

        cell_x = math.floor(x)
        cell_y = math.floor(y)
        local_x = x - cell_x
        local_y = y - cell_y 

        u = self._fade(local_x)
        v = self._fade(local_y)

        interpolated_top = self._lerp(top_left_dot_product, top_right_dot_product, u)
        interpolated_bottom = self._lerp(bottom_left_dot_product, bottom_right_dot_product, u)

        interpolated_top_and_bottom = self._lerp(interpolated_top, interpolated_bottom, v)
        return interpolated_top_and_bottom

    def get_noise(self, x: float, y: float) -> float:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise ValueError(f"coordinates ({x}, {y}) are outside of the grid | grid width/height: {self.width}/{self.height}")
        return self._interpolate_dot_products(x, y)