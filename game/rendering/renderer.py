import pygame
import game.gamestate as gamestate
import game.rendering.hud_draw as hud_draw
import game.rendering.world_draw as world_draw
import game.rendering.draw_menu as draw_menu

class Renderer():
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.font = pygame.font.Font(None, 24)

    def _render_main_menu(self):
        draw_menu.draw_main_menu(self.screen)

    def _render_game(self, session, fps, score_manager):
        # draw terrain
        world_draw.draw_terrain(self.screen, session.world, self.assets["tiles"], session.camera)
        world_draw.draw_objects(self.screen, session.world, self.assets["objects"], session.camera)

        world_draw.draw_enemies(self.screen, session.world.enemies, session.camera, self.assets["characters"])
        world_draw.draw_player(self.screen, session.player, session.camera, self.assets["characters"])

        world_draw.draw_effects(self.screen, session.world, session.camera, session.player)
        world_draw.draw_projectiles(self.screen, session.world, session.camera, session.player)

        hud_draw.draw_hud(self.screen, self.font, session.player, fps)
        hud_draw.draw_time_elapsed(self.screen, self.font, session.elapsed_time, score_manager)


    def _render_game_over(self, session, best_time):
        draw_menu.draw_game_over(self.screen, session.elapsed_time, best_time)

    def _render_level_up(self, session):
        hud_draw.draw_upgrade_choices(self.screen, self.font, session.player)

    def render(self, state, session, fps, score_manager):
        self.screen.fill((0,0,0))
         
        match state:
            case gamestate.GameState.MENU:
                self._render_main_menu()
            case gamestate.GameState.PLAYING:
                self._render_game(session, fps, score_manager)
            case gamestate.GameState.GAME_OVER:
                self._render_game_over(session, score_manager.get_best_time())
            case gamestate.GameState.PAUSED:
                ...
            case gamestate.GameState.LEVEL_UP:
                self._render_level_up(session)

        pygame.display.flip()

    def show_message(self, message):
        self.screen.fill((0,0,0))
        self._draw_centered(message)
        pygame.display.flip()
        pygame.event.pump()

    def _draw_centered(self, message):
         text = self.font.render(message, True, (255,255,255))
         self.screen.blit(text, text.get_rect(center=self.screen.get_rect().center))

