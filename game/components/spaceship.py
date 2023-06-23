import pygame
from game.components.shield import Shield
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET,SPACESHIP_SHIELD

class Bullet(Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (20, 20))  # Escala la imagen de la bala a un tamaño de 20x20 píxeles
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que representa la imagen de la bala
        self.rect.x = position[0]  # Establece la posición inicial en el eje x de la bala
        self.rect.y = position[1]  # Establece la posición inicial en el eje y de la bala

    def update(self):
        self.rect.y -= 8  # Actualiza la posición de la bala moviéndola hacia arriba

class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP  # Carga la imagen de la nave espacial
        # Escala la imagen de la nave a un tamaño de 50x60 píxeles
        self.image = pygame.transform.scale(self.image, (50, 60))  
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que representa la imagen de la nave
        self.speed = 8  # Velocidad de movimiento de la nave
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2  # Posición inicial en el eje x de la nave (centrada horizontalmente)
        self.rect.y = SCREEN_HEIGHT - self.rect.height  # Posición inicial en el eje y de la nave (parte inferior de la pantalla)
        self.bullets = []  # Lista para almacenar las balas disparadas por la nave
        self.shield = Shield()
        self.shield_active = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # Dibuja la imagen de la nave en la pantalla


    def draw_bullets(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)  # Dibuja cada bala en la pantalla

    def move_left(self, keyboard_events):
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= self.speed  # Mueve la nave hacia la izquierda según la velocidad establecida

    def move_right(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT]:
            self.rect.x += self.speed  # Mueve la nave hacia la derecha según la velocidad establecida

    def move_up(self, keyboard_events):
        if keyboard_events[pygame.K_UP]:
            self.rect.y -= self.speed  # Mueve la nave hacia arriba según la velocidad establecida

    def move_down(self, keyboard_events):
        if keyboard_events[pygame.K_DOWN]:
            self.rect.y += self.speed  # Mueve la nave hacia abajo según la velocidad establecida

    def fire_bullet(self):
        # Crea una nueva instancia de bala con la posición adecuada
        bullet = Bullet((self.rect.x + self.rect.width // 2, self.rect.y))  
        self.bullets.append(bullet)  # Agrega la bala a la lista de balas de la nave

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.bullets.clear()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()  # Actualiza la posición de cada bala moviéndola hacia arriba
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)  # Si la bala sale de la pantalla, se elimina de la lista
    
    def update(self, keyboard_events):
        self.move_up(keyboard_events)
        self.move_down(keyboard_events)
        self.move_left(keyboard_events)
        self.move_right(keyboard_events)
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))  # Limita la posición de la nave dentro de los límites de la pantalla en el eje x
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))  # Limita la posición de la nave dentro de los límites de la pantalla en el eje y
        self.update_bullets()  # Actualiza las balas disparadas por la nave
        
    def shield_collision(self):
        self.image = pygame.transform.scale(SPACESHIP_SHIELD, (50, 60))
        self.shield.kill()
        
    def normal(self):
        self.image = pygame.transform.scale(SPACESHIP, (50, 60))
        



            


