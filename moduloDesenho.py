import pygame
from moduloColisão import ColisaoMapa

class desenhar():
    def __init__(self, screen, BLACK, RED, WHITE, bullets, enemies, navins, proj, vida, lista, player):
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for enemy in enemies:
            pygame.draw.rect(screen, BLACK, enemy.rect)
        for nav in navins:
            screen.blit(nav.image, nav.rect)
        for projec in proj:
            screen.blit(projec.image, projec.rect)
        for vidas in vida:
            pygame.draw.rect(screen, RED, vidas.rect)
        ColisaoMapa.printar(lista, player)