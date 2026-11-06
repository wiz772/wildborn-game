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

def load_tile(terrain_sheet,    column, row):
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
    

def load_assets():
    assets = {}

    terrain_sheet = pygame.image.load(
        "assets/terrain.png"
    ).convert_alpha()

    assets["tiles"] = load_all_tiles(terrain_sheet)

    return assets