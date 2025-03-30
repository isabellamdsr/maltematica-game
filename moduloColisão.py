import pygame

class ColisaoMapa:
    def __init__(self):
        # Armazena os retângulos de colisão como um atributo da classe
        self.lista = [
            pygame.Rect(0, 0, 150, 810), 
            pygame.Rect(150, 0, 1140, 292),
            pygame.Rect(1290, 0, 150, 810),
            pygame.Rect(150, 744, 495, 292),
            pygame.Rect(150, 1101, 165, 66),
            pygame.Rect(795, 744, 495, 66)
        ]

    def printar(lista, player):
        for block in lista:
            if block.colliderect(player):
                print('aaaaaaaa')