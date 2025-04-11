import pygame
from moduloConfig import *

def historiaFinal():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
     
    background = pygame.image.load("spritesGT/TelaInicial.png")
    screen.blit(background, (0, 0))
    
    clock = pygame.time.Clock()

    clock.tick(60)

    while True: # Loop da tela de gamevoer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
        pygame.display.flip()