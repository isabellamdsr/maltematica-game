import pygame

class coracao():
    def __init__(self, xAxis, yAxis):
        self.image = pygame.image.load("spritesGT/coracaoCheio.png")
        self.image = pygame.transform.scale(self.image, (40,40))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(xAxis, yAxis))  # Usar o retângulo da imagem


class Player:
    def __init__(self, player_size2, player_size, WIDTH, HEIGHT):
        self.image = pygame.image.load("spritesGT/Player_idle.png")  # Carregar imagem do jogador
        self.image = pygame.transform.scale(self.image, (player_size2, player_size))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 1.3))  # Usar o retângulo da imagem

    def move(self, dx, dy, player_speed, blocos): 
        # Cria uma cópia do retângulo para testar a próxima posição
        next_rect = self.rect.copy()
        next_rect.x += dx * player_speed
        next_rect.y += dy * player_speed
        self.rect.clamp_ip(0, 0, 1440, 810)
        # Testa colisão antes de mover
        if not any(next_rect.colliderect(bloco) for bloco in blocos):
            self.rect = next_rect  # Move apenas se não houver colisão

class vidaPlayer():
    def __init__(self):
        self.tomaDanoSfx = pygame.mixer.Sound("sons/danoPlayer.mp3")
        self.curaVidaSfx = pygame.mixer.Sound("sons/coletarCura.mp3")
        self.vida = []
        self.xAtual = 1300
        self.yAtual = 100


    def adicionarCoracao(self, qntCoracoes):
        self.curaVidaSfx.play()
        for i in range(qntCoracoes):
            self.vida.append(coracao(self.xAtual, self.yAtual))
            self.xAtual -= 60
        

    def retirarCoracao(self, qntCoracoes):
            self.tomaDanoSfx.play()
            for i in range(qntCoracoes):
                self.vida.pop()