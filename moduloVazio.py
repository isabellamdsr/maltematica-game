import pygame
import random
from moduloConfig import *
#projetil settings
projetil_size = 60
projetil_speed = 12


class Vazio:
    def __init__(self, naturaisLista, WIDTH):
        self.image = pygame.image.load('spritesGT/weapon0.png')  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (projetil_size, projetil_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - projetil_size), 0))  # Usar o retângulo da imagem
    
    def move(self):
        self.rect.y += projetil_speed #Projetil cai pro inferno

    def moveVazio(self, tickSpawnVazio, a):
        if pygame.time.get_ticks() < tickSpawnVazio+(a):
            self.rect.y += projetil_speed

class explosao:
    def __init__(self, x, y):
        explosao.image = pygame.image.load('spritesGT/weaponN1.png')  # Carregar imagem do jogador
        explosao.image = pygame.transform.scale(explosao.image, (200, 200))  # Ajustar o tamanho da imagem
        explosao.rect = explosao.image.get_rect(x, y)  # Usar o retângulo da imagem