import pygame

def draw_hud(screen, font, player, fps):
    draw_coords(screen, font, player)
    draw_fps(screen, font, fps)
    draw_stats(screen, font, player)

def draw_fps(screen, font, fps):
    text = font.render(f"FPS: {fps}", True, (255,0,0))
    screen.blit(text, (10,10))

def draw_coords(screen, font, player):
    player_pos = player.position
    text_pos = font.render(f"Coords: x: {player_pos[0]}, y: {player_pos[1]}", True, (255,0,0))

    screen.blit(text_pos, (10, 50))

def draw_stats(screen, font, player):
    player_xp, player_level, player_xp_to_next = player.xp, player.level, player.xp_to_next_level
    text_pos = font.render(f"LEVEL: {player_level}, CURRENT XP: {player_xp}, XP TO NEXT: {player_xp_to_next}", True, (255,0,0))
    screen.blit(text_pos, (10, 100)) 

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