import pygame

#navin class
class NAVIN:
    def __init__(self, numeroNavin, navinLista):
        self.image = pygame.image.load(navinLista[numeroNavin])  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (267, 315))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(720, 150))  # Usar o retângulo da imagem
