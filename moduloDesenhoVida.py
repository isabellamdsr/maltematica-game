import pygame

class healthBar:
    def __init__(self):
        self.image = pygame.image.load("spritesGT/navinHealthBar.png")  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (895, 60))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(715, 750))  # Usar o retângulo da imagem
    
    def printar(self, screen):
        screen.blit(self.image, self.rect)
