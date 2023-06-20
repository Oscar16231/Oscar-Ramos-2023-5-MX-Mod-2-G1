import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    def __init__(self):
        self.images = [ENEMY_1, ENEMY_2]  # Lista de imágenes de enemigos
        self.image = pygame.transform.scale(random.choice(self.images), (50, 60))  # Seleccionar una imagen aleatoria y escalarla
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Posición inicial aleatoria en el eje x
        self.rect.y = random.randint(-self.rect.height, -10)  # Posición inicial aleatoria en el eje y (parte superior de la pantalla)
        self.speed_x = random.randint(-9, 9)  # Velocidad horizontal aleatoria
        self.speed_y = random.randint(8, 15)  # Velocidad vertical aleatoria

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x  # Mover enemigo en el eje x
        self.rect.y += self.speed_y  # Mover enemigo en el eje y

        # Verificar si el enemigo ha salido de la pantalla
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Reposicionar enemigo en el eje x
            self.rect.y = random.randint(-self.rect.height, -10)  # Reposicionar enemigo en la parte superior de la pantalla
            self.speed_x = random.randint(-9, 9)  # Generar una nueva velocidad horizontal aleatoria
            self.speed_y = random.randint(8, 15)  # Generar una nueva velocidad vertical aleatoria
            self.image = pygame.transform.scale(random.choice(self.images), (50, 60))  # Cambiar aleatoriamente la imagen del enemigo

        # Verificar si el enemigo ha alcanzado los límites de la pantalla en el eje x
        if self.rect.right > SCREEN_WIDTH:
            self.speed_x = -random.randint(1, 9)  # Cambiar la dirección del movimiento hacia la izquierda
        elif self.rect.left < 0:
            self.speed_x = random.randint(1, 9)  # Cambiar la dirección del movimiento hacia la derecha
