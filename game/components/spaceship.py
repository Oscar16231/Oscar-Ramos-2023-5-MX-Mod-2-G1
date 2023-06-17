import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT
#sprite es un objeto de pygame
class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(50,60)) #ancho y alto
        self.rect = self.image.get_rect()
        self.speed = 8  #Movimiento de la nave, velocidad de desplazamiento
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2 #Coloca la nave en el centro del eje x
        self.rect.y = (SCREEN_HEIGHT - self.rect.height) #Coloca la nave en el tope inferior de la pantalla en el eje y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_left(self,keyboard_events): #Movimiento a la derecha
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= self.speed
    
    def move_right(self,keyboard_events): #Movimiento a la izquierda
        if keyboard_events[pygame.K_RIGHT]:
            self.rect.x += self.speed
    
    def move_up(self,keyboard_events): #Movimiento hacia arriba
        if keyboard_events[pygame.K_UP]:
            self.rect.y -= self.speed
    
    def move_down(self,keyboard_events): #Movimiento hacia abajo
        if keyboard_events[pygame.K_DOWN]:
            self.rect.y += self.speed

    def update(self,keyboard_events):
        self.move_up(keyboard_events)   
        self.move_down(keyboard_events)
        self.move_left(keyboard_events)
        self.move_right(keyboard_events)
        #Limita el espacio de movimiento en el eje x al tamaño de la pantalla
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))  
        #Limita el espacio de movimiento en el eje y al tamaño de la pantalla
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

        