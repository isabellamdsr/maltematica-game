import pygame
import random

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

    def moveVazio(self, HEIGHT):
        self.rect.y += projetil_speed
