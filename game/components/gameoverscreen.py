import pygame
import sys
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE

class GameOverScreen:
    def __init__(self, restart_game):
        self.restart_game = restart_game
        self.font = pygame.font.Font(FONT_STYLE, 50)  # Fuente para el texto principal
        self.font_2 = pygame.font.Font(FONT_STYLE, 30)  # Fuente para las instrucciones
        # Renderiza el texto principal
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))  
         # Renderiza las instrucciones
        self.instruction = self.font_2.render("Press any key to continue", True, (255, 255, 255)) 
        self.score_text = None
        self.deaths = None
        self.max_score_text = None

    def show(self, screen, score, max_score, deaths):
        screen.fill((0, 0, 0))  # Limpia la pantalla con un color negro
        # Muestra el texto principal centrado en la parte superior de la pantalla
        screen.blit(self.game_over_text, (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2, SCREEN_HEIGHT // 4 - 50))
        # Muestra las instrucciones centradas en la pantalla
        screen.blit(self.instruction, (SCREEN_WIDTH // 2 - self.instruction.get_width() // 2, SCREEN_HEIGHT // 2.5 - 50))
        self.score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))  # Renderiza el texto de puntuación
        self.max_score_text = self.font.render(f"Max Score: {max_score}", True, (255, 255, 255))  # Renderiza el texto de puntuación máxima
        self.deaths = self.font.render(f"Deaths: {deaths}", True, (255, 255, 255))  # Renderiza el texto de muertes
        # Muestra los textos de puntuación, puntuación máxima y muertes centrados en la pantalla
        screen.blit(self.score_text, (SCREEN_WIDTH // 2 - self.score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(self.max_score_text, (SCREEN_WIDTH // 2 - self.max_score_text.get_width() // 2, SCREEN_HEIGHT // 1.65 + 50))
        screen.blit(self.deaths, (SCREEN_WIDTH // 2 - self.deaths.get_width() // 2, SCREEN_HEIGHT // 1.25 + 50))
        pygame.display.flip()  # Actualiza la pantalla
        self.wait_for_input()  # Espera la entrada del usuario

    def wait_for_input(self):
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                    sys.exit() #cierra el programa
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.restart_game()  # Reinicia el juego cuando se presiona una tecla o se hace clic
                    wait = False  # Sale del bucle de espera
