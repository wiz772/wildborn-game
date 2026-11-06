import pygame
import game.settings as settings
import game.entities.player as player
import world.world as world
import game.assets.asset_manager as asset_manager
import game.render as render
import game.camera as camera

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_NAME)
        self.font = pygame.font.Font(None, 24)

        self.in_game = True

        self.assets = asset_manager.load_assets()
        self.world = None

        self.player = player.Player(self)
        self.camera = camera.Camera()

        self.running = True

    def _handle_inputs(self, dt):
        keys = pygame.key.get_pressed()

        if self.in_game:
            if self.player.is_alive:
                direction = pygame.Vector2(
                    keys[pygame.K_d] - keys[pygame.K_q],
                    keys[pygame.K_s] - keys[pygame.K_z]
                )

                self.player.update(direction, dt)

    def _render_game(self):
        render.draw_terrain(self.screen, self.world, self.assets["tiles"], self.camera)
        render.draw_player(self.screen, self.player.position, self.camera)

    def _render_hud(self, clock):
        print("rendecring hud")
        fps = clock.get_fps()
        text = self.font.render(f"FPS: {fps}", True, (255,0,0))
        self.screen.blit(text, (10,10))

        player_pos = self.player.position
        text_pos = self.font.render(f"Coords: x: {player_pos[0]}, y: {player_pos[1]}", True, (255,0,0))
        self.screen.blit(text_pos, (10, 50))

    def _render_main_menu(self):
        print("game")
        self.in_game = True

    def _update(self):
        self.camera.update(self.player.position)

    def _create_world(self, size: tuple[int, int], frequency: float, seed: int | None = None):
        self.world = world.World(size, frequency, None)
        self.world.generate_random_world()

    def run(self):

        self._create_world(settings.WORLD_SIZE, 0.1, None)

        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            dt = clock.tick(settings.FPS) / 1000
            self.screen.fill((0,0,0))

            self._handle_inputs(dt)
            if self.in_game:
                self._update()
                self._render_game()
                self._render_hud(clock)
            else:
                self._render_main_menu()

                
            pygame.display.flip()

        pygame.quit()