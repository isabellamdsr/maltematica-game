import pygame

class desenhar():
    def __init__(self, screen, RED, bullets, proj, vida, player, vidaPlayer):
        for coracao in vidaPlayer:
            screen.blit(coracao.image, coracao.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for projec in proj:
            screen.blit(projec.image, projec.rect)
        for vidas in vida:
            pygame.draw.rect(screen, RED, vidas.rect)
        screen.blit(player.image, player.rect)  