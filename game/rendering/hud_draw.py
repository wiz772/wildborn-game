import pygame
import game.settings as settings

def draw_hud(screen, font, player, fps):
    draw_coords(screen, font, player)
    draw_fps(screen, font, fps)
    draw_stats(screen, font, player)

def draw_fps(screen, font, fps):
    text = font.render(f"FPS: {fps}", True, settings.HUD_TEXT_COLOR)
    screen.blit(text, (10,10))

def draw_coords(screen, font, player):
    player_pos = player.position
    text_pos = font.render(f"Coords: x: {player_pos[0]}, y: {player_pos[1]}", True, settings.HUD_TEXT_COLOR)

    screen.blit(text_pos, (10, 50))

def draw_stats(screen, font, player):
    stats_lines = [
        f"Health: {player.health} / {player.max_health}",
        f"Attack: {player.attack}",
        f"Defense: {player.defense}",
        f"Move Speed: {player.move_speed}",
        f"LEVEL: {player.level}, CURRENT XP: {player.xp} / {player.xp_to_next_level}",
    ]

    for index, stats_line in enumerate(stats_lines):
        stats_text = font.render(stats_line, True, settings.HUD_TEXT_COLOR)
        screen.blit(stats_text, (10, 100 + (20*index)))

def draw_upgrade_choices(screen, font, player):
    screen.fill((30, 30, 30))

    width, height = screen.get_size()

    card_width = 200
    card_height = 120
    spacing = 20

    total_width = len(player.choices) * card_width + (len(player.choices) - 1) * spacing
    start_x = (width - total_width) // 2
    card_y = (height - card_height) // 2

    for index, upgrade in enumerate(player.choices):
        x = start_x + index * (card_width + spacing)

        pygame.draw.rect(screen, (70, 70, 70), (x, card_y, card_width, card_height))

        title = font.render(upgrade["name"], True, (255, 255, 255))
        desc = font.render(upgrade["desc"], True, (200, 200, 200))
        keys = font.render(f"Appuie sur: {str(1 + index)}", True, (200,200,200))

        screen.blit(title, (x + 10, card_y + 30))
        screen.blit(desc, (x + 10, card_y + 65))
        screen.blit(keys, (x + 10, card_y - 20))