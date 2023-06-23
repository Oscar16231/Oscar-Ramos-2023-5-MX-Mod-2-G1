import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD

class Shield(Sprite):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase Sprite
        self.image = pygame.transform.scale(SHIELD, (50, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 8
        self.active = False  # Estado inicial del escudo (inactivo)
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # Dibuja la imagen del escudo en la pantalla

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:  # Verificar si ha salido completamente de la pantalla
            self.kill()
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width) 

