import pygame
import game.settings as settings
import game.entities.player as player
import world.world as world
import game.assets.asset_manager as asset_manager
import game.camera as camera
import game.gamestate as gamestate
import game.rendering.renderer as renderer
import game.session as session
import game.entities.enemy as enemy
import game.entities.enemy_spawner as spawner

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_NAME)

        self.assets = asset_manager.load_assets()

        self.renderer = renderer.Renderer(self.screen, self.assets)

        self.session: session.Session | None = None

        self.state = gamestate.GameState.MENU
        self.running = True

    def _handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if self.state == gamestate.GameState.MENU:
                self._start_game()
            elif self.state == gamestate.GameState.GAME_OVER:
                self.state = gamestate.GameState.MENU

    def _read_movement(self) -> pygame.Vector2:
        keys = pygame.key.get_pressed()
        return pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_q],
            keys[pygame.K_s] - keys[pygame.K_z]
        )

    def _update(self, dt):
        current_session = self.session
        if self.state != gamestate.GameState.PLAYING or current_session is None:
            return

        current_session.player.update(self._read_movement(), dt)
        current_session.camera.update(current_session.player.position)

        current_session.spawner.update(dt, current_session)

        for weapon in current_session.player.weapons:
            weapon.update(dt, current_session.player, current_session.world)
                
        for enemy in current_session.world.enemies:
            enemy.update(dt, current_session.player)

        current_session.world.enemies = [e for e in current_session.world.enemies if e.is_alive()]

        if not current_session.player.is_alive():
            self.state = gamestate.GameState.GAME_OVER

    def _start_game(self, world_seed=None):
        new_world = world.World(settings.WORLD_SIZE, 0.5, world_seed)
        new_world.generate_random_world()

        new_player = player.Player()
        new_camera = camera.Camera()
        new_spawner = spawner.Spawner()

        self.session = session.Session(new_world, new_player, new_spawner, new_camera)
        self.state = gamestate.GameState.PLAYING

    def run(self):
        clock = pygame.time.Clock()
        
        while self.running:
            dt = clock.tick(settings.FPS) / 1000
        
            for event in pygame.event.get():
                self._handle_events(event)

            self._update(dt)
            self.renderer.render(self.state, self.session, clock.get_fps())


        pygame.quit()