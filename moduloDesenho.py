import pygame

class desenhar():
    def __init__(self, screen, BLACK, RED, WHITE, bullets, enemies, proj, vida, lista, player, vidaPlayer, vazio):
        for coracao in vidaPlayer:
            screen.blit(coracao.image, coracao.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for enemy in enemies:
            pygame.draw.rect(screen, BLACK, enemy.rect)
        for projec in proj:
            screen.blit(projec.image, projec.rect)
        for vidas in vida:
            pygame.draw.rect(screen, RED, vidas.rect)