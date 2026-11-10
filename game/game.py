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

        current_session.player.update(self._read_movement(), dt)
        current_session.camera.update(current_session.player.position)
        current_session.spawner.update(dt, current_session)

        current_session.elapsed_time += dt

        for weapon in current_session.player.weapons:
            weapon.update(dt, current_session.player, current_session.world)
        
        for enemy in current_session.world.enemies:
            enemy.update(dt, current_session.player)

        for e in current_session.world.enemies:
            if not e.is_alive():
                current_session.player.add_xp(e.xp_reward)

        if current_session.player.pending_upgrade > 0:
            self.state = gamestate.GameState.LEVEL_UP
            current_session.player.choices.extend(upgrades.random_upgrades(current_session.player))

        current_session.world.enemies = [e for e in current_session.world.enemies if e.is_alive()]

        if current_session.player.damage_received:
            current_session.camera.shake(intensity=8, duration=0.2)
            current_session.player.damage_received = False

        current_session.camera.update_shake(dt)

        for effect in current_session.world.effects:
            effect.update(dt)

        current_session.world.effects = [
            effect for effect in current_session.world.effects
            if effect.is_alive()
        ]

        for projectile in current_session.world.projectiles:
            projectile.update(dt, current_session.world.enemies)

        current_session.world.projectiles = [
            p for p in current_session.world.projectiles
            if p.active
        ]

        if not current_session.player.is_alive():
            self.score_manager.add_new_score(current_session.elapsed_time)
            self.state = gamestate.GameState.GAME_OVER

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