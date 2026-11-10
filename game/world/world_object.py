from dataclasses import dataclass

@dataclass
class WorldObject:
    x: int
    y: int
    kind: str
    variant: int = 0
    opened: bool = False