import pygame
from moduloConfig import *

class Coletavel: # coletar as armas que serão dropadas a cada final de fase
    def __init__(self,armaItem):
        self.image = pygame.image.load(armaItem) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(720, 290))
        self.coletou = False
    
    def coleta(self, player, inventarioArmas, arma):
        if self.rect.colliderect(player) == False and self.coletou == False:
            screen.blit(self.image, self.rect)  
        if self.rect.colliderect(player):
            self.coletou = True
            inventarioArmas.append(arma)

class Metralhadora(Coletavel): # drop da fase 1
    def __init__(self):
        metralhadoraImg = "spritesGT/weaponN1.png"
        super().__init__(metralhadoraImg)
        self.image = pygame.image.load(metralhadoraImg) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(720, 290))
        self.coletou = False

class Bazuca(Coletavel):
    def __init__(self):
        bazucaImg = "spritesGT/weapon0.png"        
        super().__init__(bazucaImg)
        self.image = pygame.image.load(bazucaImg) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(370, 315))
        self.coletou = False

class Shotgun(Coletavel): # drop da fase 2
    def __init__(self):
        shotgunImg = "spritesGT/weaponR1.png"      
        super().__init__(shotgunImg)
        self.image = pygame.image.load(shotgunImg) 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(1073, 315))
        self.coletou = False

class iconePistola():
    def __init__(self):
        self.image = pygame.image.load("spritesGT/weapon1.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(50, 50))  # Usar o retângulo da imagem
class iconeMetra():
    def __init__(self):
        self.image = pygame.image.load("spritesGT/weaponN1.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(100, 50))  # Usar o retângulo da imagem
class iconeBazuca():
    def __init__(self):
        self.image = pygame.image.load("spritesGT/weapon0.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(150, 50))  # Usar o retângulo da imagem
class iconeEscopeta():
    def __init__(self):
        self.image = pygame.image.load("spritesGT/weaponR1.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(200, 50))  # Usar o retângulo da imagem

def printColetaveis(inventario, pist, metra, bazuca, escopeta):
    if pist in inventario:
        screen.blit(iconePistola().image, iconePistola().rect)
    if metra in inventario:
        screen.blit(iconeMetra().image, iconeMetra().rect)
    if bazuca in inventario:
        screen.blit(iconeBazuca().image, iconeBazuca().rect)
    if escopeta in inventario:
        screen.blit(iconeEscopeta().image, iconeEscopeta().rect)