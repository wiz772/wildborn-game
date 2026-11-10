import pygame

def draw_main_menu(screen):
    width, height = screen.get_size()
    center_x = width // 2

    background = (13, 23, 22)
    forest = (20, 43, 35)
    gold = (219, 181, 105)
    white = (235, 232, 216)
    muted = (145, 157, 143)

    if not hasattr(draw_main_menu, "gradient_surf") or draw_main_menu.gradient_size != (width, height):
        draw_main_menu.gradient_surf = pygame.Surface((width, height))
        for y in range(height):
            t = y / height
            color = (int(13 + t * 8), int(23 + t * 15), int(22 + t * 5))
            pygame.draw.line(draw_main_menu.gradient_surf, color, (0, y), (width, y))
        draw_main_menu.gradient_size = (width, height)
    screen.blit(draw_main_menu.gradient_surf, (0, 0))

    for radius, alpha in [(280, 15), (220, 20), (160, 25)]:
        glow = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(glow, (*gold, alpha), (radius, radius), radius)
        screen.blit(glow, (center_x - radius, height // 3 - radius))

    pygame.draw.polygon(
        screen, forest,
        [
            (0, height * 0.75), (width * 0.2, height * 0.60),
            (width * 0.4, height * 0.77), (width * 0.65, height * 0.58),
            (width, height * 0.76), (width, height), (0, height)
        ]
    )
    pygame.draw.polygon(
        screen, (16, 34, 29),
        [
            (0, height * 0.85), (width * 0.25, height * 0.72),
            (width * 0.5, height * 0.86), (width * 0.8, height * 0.70),
            (width, height * 0.84), (width, height), (0, height)
        ]
    )

    if not hasattr(draw_main_menu, "fonts"):
        draw_main_menu.fonts = {
            'title': pygame.font.Font(None, 112),
            'subtitle': pygame.font.Font(None, 25),
            'text': pygame.font.Font(None, 34),
            'footer': pygame.font.Font(None, 23)
        }
    f = draw_main_menu.fonts

    title = f['title'].render("WILDBORN", True, white)
    title_rect = title.get_rect(center=(center_x, int(height * 0.29)))
    screen.blit(title, title_rect)

    pygame.draw.line(
        screen, gold,
        (center_x - 115, title_rect.bottom + 12),
        (center_x + 115, title_rect.bottom + 12), 2
    )

    subtitle = f['subtitle'].render("SURVIVE. ADAPT. DOMINATE.", True, gold)
    screen.blit(subtitle, subtitle.get_rect(center=(center_x, title_rect.bottom + 42)))

    prompt_text = f['text'].render("Appuyez sur Entrée pour commencer", True, white)
    screen.blit(prompt_text, prompt_text.get_rect(center=(center_x, int(height * 0.65))))

    footer = f['footer'].render("A WILD WORLD AWAITS YOU", True, muted)
    screen.blit(footer, footer.get_rect(center=(center_x, height - 40)))

def draw_game_over(screen, time_elapsed, best_time):
    screen_width, screen_height = screen.get_size()
    center_x = screen_width // 2

    title_font = pygame.font.Font(None, 80)
    stats_font = pygame.font.Font(None, 36)
    controls_font = pygame.font.Font(None, 28)

    title = title_font.render("GAME OVER", True, (220, 60, 60))
    screen.blit(title, title.get_rect(center=(center_x, screen_height // 2 - 120)))

    survival = stats_font.render(
        f"Survival Time: {time_elapsed:.1f}s",
        True,
        (255, 255, 255)
    )
    screen.blit(survival, survival.get_rect(center=(center_x, screen_height // 2 - 30)))

    best = stats_font.render(
        f"Best Time: {best_time:.1f}s",
        True,
        (255, 215, 0)
    )
    screen.blit(best, best.get_rect(center=(center_x, screen_height // 2 + 20)))

    controls = controls_font.render(
        "ENTER - Restart     ESC - Main Menu",
        True,
        (170, 170, 170)
    )
    screen.blit(controls, controls.get_rect(center=(center_x, screen_height // 2 + 120)))