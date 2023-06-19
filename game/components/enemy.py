import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1,ENEMY_2,SCREEN_HEIGHT,SCREEN_WIDTH

class Enemy(Sprite):
    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(50,60)) #ancho y alto
        self.rect = self.image.get_rect()
        #self.speed = 9  #Movimiento de la nave, velocidad de desplazamiento
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2 #Coloca al enemigo en el centro del eje x
        #Coloca al enemigo en el tope superior de la pantalla en el eje y
        self.rect.y = (SCREEN_HEIGHT - self.rect.height) // 64 
        self.speed_x = random.randint(9, 12)  # Generar una velocidad aleatoria en el eje x
        self.speed_y = random.randint(9, 12)  # Generar una velocidad aleatoria en el eje y


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self):
        # Mover el enemigo en ambas direcciones
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Verificar si el enemigo ha alcanzado los límites de la pantalla
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            # Invertir la velocidad en el eje x
            self.speed_x = -self.speed_x
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            # Invertir la velocidad en el eje y
            self.speed_y = -self.speed_y