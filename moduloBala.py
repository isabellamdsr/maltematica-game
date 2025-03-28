import pygame
import math

#bullet class
class Bullet:
    def __init__(self, x, y,bullet_size, danoBala, anguloBala):
        self.anguloBala = anguloBala
        self.danoBala = danoBala
        self.image = pygame.image.load("spritesGT/1 pixelado.webp")  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (bullet_size, bullet_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(x, y))  # Usar o retângulo da imagem

    def move(self,bullet_speed, anguloBala):
        radAngulo =math.radians(anguloBala)
        self.rect.y -= (math.sin(radAngulo) * bullet_speed) #Bullet sai do bloco player e vai ao além pra cima
        self.rect.x -= (math.cos(radAngulo) * bullet_speed) 
    