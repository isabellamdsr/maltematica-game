import pygame

class healthBar:
    def __init__(self):
        self.image = pygame.image.load("spritesGT/navinHealthBar_3.png").convert_alpha()  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (890, 60))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(719, 751))  # Usar o retângulo da imagem
    
    def printar(self, screen):
        screen.blit(self.image, self.rect)