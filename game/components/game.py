import pygame
from random import randint
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE,SOUND,FONT_STYLE
from game.components.spaceship import Spaceship
#Game tiene un spaceship (una instancia de una clase Spaceship)
#Game puede decirle al spaceship que se actualize llamando al metodo update(), update espera una lista que contiene
#los eventos del teclado que pudieron haber ocurrido

#Game ahora tiene un enemy
#Game puede decirle al spaceship que se actualize llamando al metodo update()
from game.components.enemy import Enemy

from game.components.gameoverscreen import GameOverScreen
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemies = [] # Lista para almacenar los enemigos
        #Genera 5 enemigos y los almacena en la lista
        for _ in range(5):
            enemy = Enemy()
            self.enemies.append(enemy)
        self.sounds = SOUND
        self.game_over_screen = GameOverScreen(self.restart_game)  # Agregar la pantalla de Game Over
        self.score = 0
        self.deaths = 0
        self.max_score = 0
        self.font = pygame.font.Font(FONT_STYLE, 40)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!\nBYE BYE!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceship.fire_bullet()
        
    def update(self):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        for enemy in self.enemies:
            enemy.update()
            if randint(1, 20) == 1:
                enemy.fire_bullet()
        self.handle_collisions()
        if not self.enemies:
            self.spawn_enemies()
    
    def handle_collisions(self):
        for bullet in self.spaceship.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.spaceship.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.sounds.play()
                    self.score += 100
                    self.deaths += 1
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if bullet.rect.colliderect(self.spaceship.rect):
                    self.game_over()
        if pygame.sprite.spritecollide(self.spaceship, self.enemies, False):
            self.game_over()
        

    def spawn_enemies(self):
        for _ in range(5):
            enemy = Enemy()
            self.enemies.append(enemy)

    def game_over(self):
        self.playing = False
        self.max_score = max(self.score, self.max_score)
        self.game_over_screen.show(self.screen, self.score, self.max_score, self.deaths)
        self.score = 0
        self.deaths = 0
        self.spaceship.reset()
        self.enemies.clear()

    def restart_game(self):
        self.playing = True
    
    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        #yo "Game" se dibujar mi escenario
        self.draw_background()
        #yo "Game" le ordeno al spaceship dibujarse llamando a un metodo draw del Spaceship
        #el metodo draw espera que le pase el screen
        self.spaceship.draw(self.screen)
        #yo "Game" le ordeno al enemy dibujarse varias veces llamando a un metodo draw del Enemy
        #el metodo draw espera que le pase el screen
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.draw_score() #Dibuja el score
        self.spaceship.draw_bullets(self.screen) #dibuja las balas
        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_text, score_rect)