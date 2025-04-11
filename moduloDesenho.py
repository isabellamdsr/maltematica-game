import pygame

class desenhar():
    def __init__(self, screen, RED, bullets, proj, vida, player, vidaPlayer):
        for coracao in vidaPlayer:
            screen.blit(coracao.image, coracao.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for projec in proj:
            screen.blit(projec.image, projec.rect)
        screen.blit(player.image, player.rect)  
        for vidas in vida:
            pygame.draw.rect(screen, RED, vidas.rect)

class escada:
    def __init__(self):
        self.image = pygame.image.load("spritesGT/escada.png")  # Carregar imagem do contorno
        self.image = pygame.transform.scale(self.image, (93, 246))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(380, 300))  # Usar o retângulo da imagem
