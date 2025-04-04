import pygame

class coracao():
    def __init__(self, xAxis, yAxis):
        self.image = pygame.image.load("spritesGT/coracaoCheio.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(xAxis, yAxis))  # Usar o retângulo da imagem
