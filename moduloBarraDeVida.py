import pygame

#barra de vida class
class barraDeVida:
    def __init__(self, danado, vida):
        self.rect = pygame.Rect(320, 734, 800-(danado*(800/vida)), 30) #Rect da barra e vida

class healthBar:
    def __init__(self):
        self.image = pygame.image.load("spritesGT/navinHealthBar_3.png").convert_alpha()  # Carregar imagem do contorno
        self.image = pygame.transform.scale(self.image, (890, 70))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(717, 751))  # Usar o retângulo da imagem
    
    def printar(self, screen):
        screen.blit(self.image, self.rect)