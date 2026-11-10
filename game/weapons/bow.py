from game.weapons.weapon import Weapon
from game.effects.projectile import Projectile

BOW_BASE_DMG = 5
BOW_BASE_RANGE = 150
BOW_BASE_COOLDOWN = 1

class Bow(Weapon):
    def __init__(self):
        super().__init__(BOW_BASE_DMG, BOW_BASE_RANGE, BOW_BASE_COOLDOWN)

    def attack(self, player, world):
        targets = []
        available_enemies = [
            enemy for enemy in world.enemies
            if enemy.is_alive()
        ]

        for _ in range(player.projectile_count):
            if not available_enemies:
                break

            target = min(
                available_enemies,
                key=lambda enemy: player.position.distance_to(enemy.position)
            )

            dist = player.position.distance_to(target.position)

            if dist > self.attack_range:
                break

            targets.append(target)
            available_enemies.remove(target)

        if not targets:
            return False

        for target in targets:
            world.projectiles.append(
                Projectile(
                    player.position,
                    target,
                    self.damage + player.attack
                )
            )

        return True