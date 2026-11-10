from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage: int, attack_range: float, cooldown: float):
        self.damage = damage
        self.attack_range = attack_range
        self.cooldown = cooldown
        self.timer = 0
        self.area_size = 50

    def update(self, dt, player, world):
        self.timer -= dt
        if self.timer <= 0 and self.attack(player, world):
            self.timer = self.cooldown

    @abstractmethod
    def attack(self, player, world) -> bool:
        # renvoyer true si un ennemi est touché
        ...  