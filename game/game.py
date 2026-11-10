import pygame
import settings
import game.entities.player as player
import game.world.world as world
import game.assets.asset_manager as asset_manager
import game.camera as camera
import game.gamestate as gamestate
import game.rendering.renderer as renderer
import game.session as session
import game.entities.enemy_spawner as spawner
import game.upgrades as upgrades
import game.score_manager as score_manager
import game.game_utils as game_utils

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_NAME)

        self.assets = asset_manager.load_assets()
        self.renderer = renderer.Renderer(self.screen, self.assets)

        self.session: session.Session | None = None
        self.score_manager = score_manager.ScoreManager()

        self.state = gamestate.GameState.MENU
        self.running = True

    def _handle_events(self, event):
        if event.type == pygame.QUIT:
            self._on_quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.state in (gamestate.GameState.MENU, gamestate.GameState.GAME_OVER):
                    self._start_game()

            if self.state == gamestate.GameState.LEVEL_UP:
                index = settings.CHOICE_KEYS.get(event.scancode)
                if index is not None:
                    self._choose_upgrade(index)

            if event.key == pygame.K_ESCAPE and self.state == gamestate.GameState.GAME_OVER:
                self.state = gamestate.GameState.MENU

    def _choose_upgrade(self, index):
        if self.session is not None:
            upgrades = self.session.player.choices
            upgrade = upgrades[index]
            upgrade["apply"](self.session.player)
            self.session.player.upgrades.append(upgrade)
            upgrades.clear()
            self.session.player.pending_upgrade -= 1
            self.state = gamestate.GameState.PLAYING

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

        game_utils.update_player(
            current_session, self._read_movement(), dt
        )
        game_utils.update_world(current_session, dt)
        game_utils.update_weapons(current_session, dt)
        game_utils.update_effects(current_session, dt)
        game_utils.update_projectiles(current_session, dt)

        self.state = game_utils.update_game_state(
            current_session, self.score_manager
        )

    def _start_game(self, world_seed=None):
        self.renderer.show_message(f"Generating world...")
        new_world = world.World(settings.WORLD_SIZE, 0.5, world_seed)
        new_world.generate_random_world()

        new_player = player.Player()
        new_camera = camera.Camera()
        new_spawner = spawner.Spawner()

        start_time = 0.0

        self.session = session.Session(new_world, new_player, new_spawner, new_camera, start_time)
        self.state = gamestate.GameState.PLAYING

    def _on_quit(self):
        self.score_manager.save_score()
        self.running = False

    def run(self):
        clock = pygame.time.Clock()
        
        while self.running:
            dt = clock.tick(settings.FPS) / 1000
        
            for event in pygame.event.get():
                self._handle_events(event)

            self._update(dt)
            self.renderer.render(self.state, self.session, clock.get_fps(), self.score_manager)


        pygame.quit()