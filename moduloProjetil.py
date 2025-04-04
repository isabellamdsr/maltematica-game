import pygame
import random

#projetil settings
projetil_size = 20
projetil_speed = 12

class Projetil:
    def __init__(self, naturaisLista, WIDTH):
        self.image = pygame.image.load(naturaisLista[random.randint(0,9)])  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (projetil_size, projetil_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - projetil_size), 0))  # Usar o retângulo da imagem
    
    def move(self):
        self.rect.y += projetil_speed #Projetil cai pro inferno

