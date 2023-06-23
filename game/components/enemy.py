import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY

class Enemy(Sprite):
    def __init__(self):
        self.images = [ENEMY_1, ENEMY_2]  # Lista de imágenes de enemigos
        self.image = pygame.transform.scale(random.choice(self.images), (50, 60))  # Seleccionar una imagen aleatoria y escalarla
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Posición inicial aleatoria en el eje x
        self.rect.y = random.randint(-self.rect.height, -10)  # Posición inicial aleatoria en el eje y (parte superior de la pantalla)
        self.speed_x = random.randint(-9, 9)  # Velocidad horizontal aleatoria
        self.speed_y = random.randint(8, 15)  # Velocidad vertical aleatoria
        self.bullets = pygame.sprite.Group()  # Grupo de balas del enemigo

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.bullets.draw(screen)  # Dibujar las balas

    def update(self):
        self.rect.x += self.speed_x  # Mover enemigo en el eje x
        self.rect.y += self.speed_y  # Mover enemigo en el eje y

        # Verificar si el enemigo ha salido de la pantalla
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Reposicionar enemigo en el eje x
            self.rect.y = random.randint(-self.rect.height, -10)  # Reposicionar enemigo en la parte superior de la pantalla
            self.speed_x = random.randint(-9, 9)  # Generar una nueva velocidad horizontal aleatoria
            self.speed_y = random.randint(9, 29)  # Generar una nueva velocidad vertical aleatoria
            self.image = pygame.transform.scale(random.choice(self.images), (50, 60))  # Cambiar aleatoriamente la imagen del enemigo
        # Verificar si el enemigo ha alcanzado los límites de la pantalla en el eje x
        if self.rect.right > SCREEN_WIDTH:
            self.speed_x = -random.randint(1, 9)  # Cambiar la dirección del movimiento hacia la izquierda
        elif self.rect.left < 0:
            self.speed_x = random.randint(1, 9)  # Cambiar la dirección del movimiento hacia la derecha
        # Actualizar el movimiento de las balas
        self.bullets.update()

    def fire_bullet(self):
        bullet = BulletEnemy(self.rect.centerx, self.rect.bottom)  # Crear una instancia de bala enemiga
        self.bullets.add(bullet)  # Agregar la bala al grupo de balas del enemigo

class BulletEnemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Inicializar el objeto BulletEnemy
        # Cargar y ajustar la escala de la imagen de la bala
        self.image = pygame.transform.scale(BULLET_ENEMY, (15, 15))
        # Obtener el rectángulo que ocupa la imagen de la bala
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del centro de la bala
        self.rect.centerx = x
        self.rect.centery = y
        # Establecer la velocidad vertical de la bala
        self.speed_y = 16

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:  # Verificar si la bala ha salido de la pantalla
            self.kill()  # Eliminar la bala