import pygame
pygame.init()

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Screen dimensions
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def game_over_screen():
    screen.fill(BLACK)
    
    # Renderizar textos
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    retry_text = small_font.render("Pressione ESPAÇO para jogar novamente", True, WHITE)
    retry_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    quit_text = small_font.render("Pressione ESC para sair", True, WHITE)
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

    # Desenhar na tela
    screen.blit(text, text_rect)
    screen.blit(retry_text, retry_rect)
    screen.blit(quit_text, quit_rect)
    
    pygame.display.flip()
keys = pygame.key.get_pressed()

while keys!=keys[pygame.K_0]:
    game_over_screen()