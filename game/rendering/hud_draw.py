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