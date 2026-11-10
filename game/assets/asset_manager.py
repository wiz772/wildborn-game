import pygame

TILE_SIZE = 32

TERRAIN_LAYOUT = {
    "grass": (0, 0),
    "dark_grass": (0, 1),
    "light_grass": (0, 2),
    "dirt": (0, 3),
    "sand": (0, 4),
    "stone": (0, 5),
}

def load_tile(terrain_sheet, column, row):
    rect = pygame.Rect(
        column * TILE_SIZE,
        row * TILE_SIZE,
        TILE_SIZE,
        TILE_SIZE
    )
    return terrain_sheet.subsurface(rect).copy()

def load_all_tiles(terrain_sheet):
    return {
        name: load_tile(terrain_sheet, column, row)
        for name, (column, row) in TERRAIN_LAYOUT.items()
    }

def load_trees():
    tree_sheet = pygame.image.load("assets/objects/trees.png").convert_alpha()
    return [tree_sheet.subsurface(pygame.Rect(i * 64, 0, 64, 64)).copy() for i in range(3)]

def load_characters():
    characters = {}

    for character in ("bear", "boar", "fox", "wolf", "player"):
        sheet = pygame.image.load(
            f"assets/characters/{character}.png"
        ).convert_alpha()

        frame_width = sheet.get_width() // 4
        frame_height = sheet.get_height() // 4

        characters[character] = [
            [
                sheet.subsurface(pygame.Rect(
                    column * frame_width,
                    row * frame_height,
                    frame_width,
                    frame_height
                )).copy()
                for column in range(4)
            ]
            for row in range(4)
        ]

    return characters

def load_assets():
    assets = {}

    terrain_sheet = pygame.image.load(
        "assets/tiles/terrain.png"
    ).convert_alpha()

    assets["tiles"] = load_all_tiles(terrain_sheet)
    assets["objects"] = {
        "tree": load_trees(),
    }
    assets["characters"] = load_characters()

    return assets