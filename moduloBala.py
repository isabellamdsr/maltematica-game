import pygame
import math
from moduloConfig import naturaisLista
import random

#bullet class
class Bullet:
    def __init__(self, x, y,bullet_size, danoBala, anguloBala, velocidadeBala, arma):
        self.velocidadeBala = velocidadeBala
        self.anguloBala = anguloBala
        self.danoBala = danoBala
        if arma=='pistola':
            self.image = pygame.image.load("spritesGT/1 pixelado.webp")  # Carregar imagem do pistola
        if arma=='metralhadora':
            self.image = pygame.image.load(naturaisLista[random.randint(0,9)])  # Carregar imagem do metralhadora
        if arma=='bazuca':
            self.image = pygame.image.load("spritesGT/Naturais/0_5.png")  # Carregar imagem do bazuca
        if arma=='escopeta':
            self.image = pygame.image.load("spritesGT/weapon0.png")  # Carregar imagem do escopeta
            
        self.image = pygame.transform.scale(self.image, (bullet_size, bullet_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(x, y))  # Usar o retângulo da imagem

    def move(self,bullet_speed, anguloBala):
        radAngulo =math.radians(anguloBala)
        self.rect.y -= (math.sin(radAngulo) * bullet_speed) #Bullet sai do bloco player e vai ao além pra cima
        self.rect.x -= (math.cos(radAngulo) * bullet_speed) #Bullet sai do jogador na diagonal, se preciso
    