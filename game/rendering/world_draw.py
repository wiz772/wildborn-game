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

def draw_objects(screen, world, sprites, camera):
    cam_x, cam_y = round(camera.position.x), round(camera.position.y)
    sw, sh = screen.get_size()

    for obj in world.objects:
        sprite = sprites[obj.kind][obj.variant]
        w, h = sprite.get_size()
        sx = obj.x * TILE_SIZE + TILE_SIZE // 2 - w // 2 - cam_x
        sy = (obj.y + 1) * TILE_SIZE - h - cam_y                   
        if -w < sx < sw and -h < sy < sh:                          
            screen.blit(sprite, (sx, sy))

def draw_player(screen, position: pygame.Vector2, camera):
    screen_position = position - camera.position
    pygame.draw.rect(screen, (255,0,0), (*screen_position, 32, 32))

def draw_enemies(screen, enemies, camera):
    for enemy in enemies:
        position = enemy.position - camera.position 
        pygame.draw.rect(screen, (255,40,0), (round(position.x), round(position.y), 32, 32))


