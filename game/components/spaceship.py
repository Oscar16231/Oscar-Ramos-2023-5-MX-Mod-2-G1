import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP
#sprite es un objeto de pygame
class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(50,60)) #ancho y alto
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self,keyboard_events):
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= 10  # Mover hacia la izquierda
        if keyboard_events[pygame.K_RIGHT]:
            self.rect.x += 10  # Mover hacia la derecha
        
        