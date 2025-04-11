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
    def __init__(self, WIDTH):
        self.image = pygame.image.load('spritesGT/bombaVazio.png')  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (60, 60))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(150, WIDTH - 160), 0))  # Usar o retângulo da imagem
    
    def printar(self, vazio):
        for projV in vazio:
            screen.blit(projV.image, projV.rect)

    def moveVazio(self, tickSpawnVazio, a):
        if pygame.time.get_ticks() < tickSpawnVazio+(a):
            self.rect.y += 10

class explosao:
    def __init__(self, x, y):
        x=None

        explosao.image = pygame.image.load('spritesGT/Explosao.png')  # Carregar imagem do jogador
        explosao.image = pygame.transform.scale(explosao.image, (200, 200))  # Ajustar o tamanho da imagem
        explosao.rect = explosao.image.get_rect(x, y)  # Usar o retângulo da imagem

class Ability(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_groups):
        super().__init__(sprite_groups)
        self.image = pygame.image.load(naturaisLista[random.randint(0, 9)]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(midbottom = pos)

    def shoot(pos, sprite_groups, num_projectiles = 5, spacing_vertical = 40, spacing_horizontal = 25, spacing_primeiro_projetil = 6):

        # Linha vertical (|)
        for i in range(num_projectiles):
            y = pos[1] + i * spacing_vertical
            Ability((pos[0], y), sprite_groups)

        # Linha diagonal esquerda (/)
        for i in range(num_projectiles):
            x = pos[0] - (i + spacing_primeiro_projetil) * spacing_horizontal
            y = pos[1] + i * spacing_vertical
            Ability((x, y), sprite_groups)
                                                                                          # A diferença entre os dois for's é que a esquerda diminui X e a direitaaumenta
        # Linha diagonal direita (\)
        for i in range(num_projectiles):
            x = pos[0] + (i + spacing_primeiro_projetil) * spacing_horizontal
            y = pos[1] + i * spacing_vertical
            Ability((x, y), sprite_groups)

    def update(self): 
        self.rect.centery += 5 # O número é a velocidade do ataque
        if self.rect.top > HEIGHT:
            self.kill()
class Irra: # arma de dano em área do Navin
    def __init__(self, WIDTH):
        self.image = pygame.image.load('spritesGT/evisoExplosao.png')  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (30, 300))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(random.randint(165, WIDTH - 200), 0))  # Usar o retângulo da imagem
    
    def printar(self, vazio):
        for projV in vazio:
            screen.blit(projV.image, projV.rect)

    def moveIrra(self, tickSpawnIrra, aleatorio, player):

        if pygame.time.get_ticks() < tickSpawnIrra+(aleatorio) and self.rect.colliderect(player)==False:
            self.rect.y += 9