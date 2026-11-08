import pygame
import game.gamestate as gamestate
import game.rendering.hud_draw as hud_draw
import game.rendering.world_draw as world_draw

class Renderer():
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.font = pygame.font.Font(None, 24)

    def _render_main_menu(self):
        self._draw_centered("Wildborn - Entrée pour jouer!")

    def _render_game(self, session):
        # draw terrain
        world_draw.draw_terrain(self.screen, session.world, self.assets["tiles"], session.camera)
        world_draw.draw_objects(self.screen, session.world, self.assets["objects"], session.camera)
        world_draw.draw_enemies(self.screen, session.world.enemies, session.camera)
        world_draw.draw_player(self.screen, session.player.position, session.camera)


    def _render_game_over(self):
        self._draw_centered("game over.")

    def render(self, state, session, fps):
        self.screen.fill((0,0,0))
         
        match state:
            case gamestate.GameState.MENU:
                self._render_main_menu()
            case gamestate.GameState.PLAYING:
                self._render_game(session)
                hud_draw.draw_hud(self.screen, self.font, session.player, fps)
            case gamestate.GameState.GAME_OVER:
                self._render_game_over()
            case gamestate.GameState.PAUSED:
                ...

        pygame.display.flip()

    def show_message(self, message):
        self.screen.fill((0,0,0))
        self._draw_centered(message)
        pygame.display.flip()
        pygame.event.pump()

    def _draw_centered(self, message):
         text = self.font.render(message, True, (255,255,255))
         self.screen.blit(text, text.get_rect(center=self.screen.get_rect().center))

