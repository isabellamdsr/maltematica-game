import pygame
import random
from moduloConfig import *


class Projetil:
    def __init__(self, naturaisLista, WIDTH):
        self.image = pygame.image.load(naturaisLista[random.randint(0,9)])  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (projetil_size, projetil_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - projetil_size), 0))  # Usar o retângulo da imagem
    
    def move(self):
        self.rect.y += projetil_speed #Projetil cai pro inferno

class Vazio: # arma de dano em área do Navin
    def __init__(self, x, WIDTH):
        self.image = pygame.image.load(x[0])  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (60, 60))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - 60), 0))  # Usar o retângulo da imagem
    
    def printar(self, vazio):
        for projV in vazio:
            screen.blit(projV.image, projV.rect)

    def moveVazio(self, tickSpawnVazio, a):
        if pygame.time.get_ticks() < tickSpawnVazio+(a):
            self.rect.y += projetil_speed

class explosao:
    def __init__(self, x, y):
        x=None

        explosao.image = pygame.image.load('spritesGT/Explosao.png')  # Carregar imagem do jogador
        explosao.image = pygame.transform.scale(explosao.image, (200, 200))  # Ajustar o tamanho da imagem
        explosao.rect = explosao.image.get_rect(x, y)  # Usar o retângulo da imagem
