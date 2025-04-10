import pygame
from moduloConfig import screen

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