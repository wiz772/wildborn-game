
import pygame

TILE_SIZE = 32

def draw_terrain(screen, world, tiles, camera):
    for y, row in enumerate(world.terrains):
        for x, terrain in enumerate(row):
            tile = tiles[terrain]
            screen_position = (
                pygame.Vector2(x * TILE_SIZE, y * TILE_SIZE)
                - camera.position
                + camera.shake_offset
            )

            screen.blit(tile, screen_position)


def draw_objects(screen, world, sprites, camera):
    cam_x = round(camera.position.x - camera.shake_offset.x)
    cam_y = round(camera.position.y - camera.shake_offset.y)
    sw, sh = screen.get_size()

    for obj in world.objects:
        sprite = sprites[obj.kind][obj.variant]
        w, h = sprite.get_size()

        sx = obj.x * TILE_SIZE + TILE_SIZE // 2 - w // 2 - cam_x
        sy = (obj.y + 1) * TILE_SIZE - h - cam_y

        if -w < sx < sw and -h < sy < sh:
            screen.blit(sprite, (sx, sy))


def draw_player(screen, player, camera, characters):
    screen_position = (
        player.position - camera.position + camera.shake_offset
    )
    sprite = characters["player"][player.direction][player.frame]

    screen.blit(sprite, (round(screen_position.x), round(screen_position.y)))


def draw_enemies(screen, enemies, camera, characters):
    for enemy in enemies:
        position = (
            enemy.position - camera.position + camera.shake_offset
        )
        sprite = characters[enemy.kind][enemy.direction][enemy.frame]

        screen.blit(sprite, (round(position.x), round(position.y)))


def draw_effects(screen, world, camera):
    for effect in world.effects:
        effect.draw(screen, camera)

def draw_projectiles(screen, world, camera):
    for projectile in world.projectiles:
        projectile.draw(screen, camera)