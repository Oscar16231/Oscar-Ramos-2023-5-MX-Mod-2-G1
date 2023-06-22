import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


class GameOverScreen:
    def __init__(self, restart_game):
        self.restart_game = restart_game
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.font_2 = pygame.font.Font(FONT_STYLE, 30)
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.instruction = self.font_2.render("Press any key to continue", True, (255, 255, 255))
        self.score_text = None
        self.deaths = None
        self.max_score_text = None

    def show(self, screen, score, max_score, deaths):
        screen.fill((0, 0, 0))
        screen.blit(self.game_over_text, (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2, SCREEN_HEIGHT // 4 - 50))
        screen.blit(self.instruction, (SCREEN_WIDTH // 2 - self.instruction.get_width() // 2, SCREEN_HEIGHT // 2.5 - 50))
        self.score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.max_score_text = self.font.render(f"Max Score: {max_score}", True, (255, 255, 255))
        self.deaths = self.font.render(f"Deaths: {deaths}", True, (255, 255, 255))
        screen.blit(self.score_text, (SCREEN_WIDTH // 2 - self.score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(self.max_score_text, (SCREEN_WIDTH // 2 - self.max_score_text.get_width() // 2, SCREEN_HEIGHT // 1.65 + 50))
        screen.blit(self.deaths, (SCREEN_WIDTH // 2 - self.deaths.get_width() // 2, SCREEN_HEIGHT // 1.25 + 50))
        pygame.display.flip()
        self.wait_for_input()

    def wait_for_input(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.restart_game()
                    waiting = False

