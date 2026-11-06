import pygame
import game.settings as settings
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.WINDOW_NAME)
        self.in_game = False

        self.world = None
        self.player = None

        self.running = True

    def _handle_inputs(self):
        keys = pygame.key.get_pressed()
        ...

    def _render_game(self):
        ...

    def _render_main_menu(self):
        print("game")
        self.in_game = True

    def _update(self):
        # update player
        # update animaux 
        # check collisions
        ...

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self._handle_inputs()
            if self.in_game:
                self._update()
                self._render_game()
            else:
                self._render_main_menu()

                
            pygame.display.flip()
            clock.tick(settings.FPS)

        pygame.quit()