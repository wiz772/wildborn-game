from game.weapons.weapon import Weapon
from game.effects.auraeffect import AuraEffect

AURA_BASE_DMG = 5
AURA_BASE_SIZE = 50
AURA_BASE_COOLDOWN = 1

class Aura(Weapon):
    def __init__(self):
        super().__init__(AURA_BASE_DMG, 0, AURA_BASE_COOLDOWN)
        self.area_size = AURA_BASE_SIZE
        self.effect = AuraEffect(self)  

    def attack(self, player, world) -> bool:
        if self.effect not in world.effects:
            world.effects.append(self.effect)
            
        hit = False

        for enemy in world.enemies:
            if not enemy.is_alive():
                continue

            dist = player.position.distance_to(enemy.position)

            if dist <= self.area_size:
                enemy.take_damage(self.damage + player.attack)
                hit = True

        if hit:
            self.effect.pulse()

        return hit