from game.weapons.weapon import Weapon
from game.effects.claw_effect import ClawEffect


class Claws(Weapon):
    def __init__(self):
        super().__init__(3, 48, 0.8)

    def attack(self, player, world) -> bool:
        target, best = None, self.attack_range

        for enemy in world.enemies:
            dist = player.position.distance_to(enemy.position)

            if dist <= best:
                best, target = dist, enemy

        if target is None:
            return False

        target.take_damage(self.damage + player.attack)

        world.effects.append(
            ClawEffect(player.position, target.position)
        )

        return True