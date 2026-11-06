class Entity:
    def __init__(self, health: int, max_health: int, defense: int, attack: int, move_speed: float, entity_type):
        self.health = health
        self.max_health = max_health
        self.defense = defense
        self.attack = attack
        self.move_speed = move_speed
        self.entity_type = entity_type

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int):
        damage = max(0, amount - self.defense)
        self.health -= damage

    def heal(self, amount: int):
        self.health = max(self.max_health, self.health + amount)
