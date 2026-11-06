TERRAIN_RULES = [
    (-0.15, "rock"),
    (0.0, "dirt"),
    (0.2, "grass"),
]


def get_terrain(noise_value: float):
    for key, terrain in TERRAIN_RULES:
        if noise_value <= key:
            return terrain

    return TERRAIN_RULES[-1][1]
    
