from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage: int, attack_range: float):
        self.damage = damage
        self.attack_range = attack_range

    @abstractmethod
    def attack(self, player, world):

        ...  