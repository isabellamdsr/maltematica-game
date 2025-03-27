import pygame


class Player:
    def __init__(self, player_size2, player_size, WIDTH, HEIGHT):
        self.image = pygame.image.load("spritesGT/Player_idle.png")  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (player_size2, player_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Usar o retângulo da imagem

    def move(self, dx, dy, player_speed): 
        self.rect.x += dx * player_speed    # Player andar em x
        self.rect.y += dy * player_speed    # Player andar em y
        self.rect.clamp_ip(150, 291, 1140, 453)  # Mantém o jogador dentro do local "andavel"
