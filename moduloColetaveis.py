import pygame
from moduloConfig import *

class Coletavel: # coletar as armas que serão dropadas a cada final de fase
    def __init__(self,armaItem):
        self.image = pygame.image.load(armaItem) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(720, 290))
        self.coletou = False
    
    def coleta(self,player, inventario, arma):
        if self.rect.colliderect(player) == False and self.coletou == False:
            screen.blit(self.image, self.rect)  
        if self.rect.colliderect(player):
            self.coletou = True
            inventario.append(arma)

class Metralhadora(Coletavel): # drop da fase 1
    def __init__(self):
        metralhadoraImg = "spritesGT/weaponN1.png"
        super().__init__(metralhadoraImg)
        self.image = pygame.image.load(metralhadoraImg) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(720, 290))
        self.coletou = False

class Bazuca(Coletavel):
    pass

class Shotgun(Coletavel): # drop da fase 2
    shotgunImg = "spritesGT/weaponR1.png"
    pass
