import pygame

TILE_SIZE = 32

def draw_terrain(screen, world, tiles, camera):
    for y, row in enumerate(world.terrains):
        for x, terrain in enumerate(row):
            tile = tiles[terrain]
            screen_position = pygame.Vector2(
                x * TILE_SIZE,
                y * TILE_SIZE
            ) - camera.position

            screen.blit(tile, screen_position)

def draw_objects(screen, world, trees, camera):
    ...

def draw_player(screen, position: pygame.Vector2, camera):
    screen_position = position - camera.position
    pygame.draw.rect(screen, (255,0,0), (*screen_position, 32, 32))

