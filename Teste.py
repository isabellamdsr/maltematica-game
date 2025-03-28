#Imports
import pygame
import random
from moduloPlayer import Player
from moduloBarraDeVida import barraDeVida
from moduloNAVIN import NAVIN
from moduloEnemy import Enemy
from moduloBala import Bullet
from moduloProjetil import Projetil
from moduloArmaAtiva import armaAtiva

#Comando pygame (NAO TOQUE)
pygame.init()

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

#Tela 
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

#Lista naturais
naturaisLista=['spritesGT/Naturais/zero.png','spritesGT/Naturais/um.webp','spritesGT/Naturais/dois.png',
               'spritesGT/Naturais/tres.png','spritesGT/Naturais/quatro.png','spritesGT/Naturais/cinco.png',
               'spritesGT/Naturais/seis.png','spritesGT/Naturais/sete.png','spritesGT/Naturais/oito.png',
               'spritesGT/Naturais/nove.png']

#Lista animacao navin
navinLista=['spritesGT/navin/navin_idle.png','spritesGT/navin/navin_idle2.png','spritesGT/navin/navin_idle3.png','spritesGT/navin/navin_idle4.png']

#Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

dano = 3000
#player config
player_size = 66
player_size2 = 60
player_speed = 10

#bullet config
bullet_size = 21
bullet_speed = 20

#enemy settings
enemy_size = 50
enemy_speed = 2

#projetil settings
projetil_size = 20
projetil_speed = 12


#tela de gameover (sera completamente alterado quando o sprite de tela de gameover for inserido)
def game_over_screen(rodando):
    keys = pygame.key.get_pressed()
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    main()
                    return


# Main game loop
def main():
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_1.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo
    pygame.mixer.music.load("soundtrack/SoundtrackJogo.mpga")
    pygame.mixer.music.play()


    clock = pygame.time.Clock()
    player = Player(player_size2, player_size, WIDTH, HEIGHT)
    dano = 3000     #vida do navin
    #Lista de objetos moviveis gerados
    bullets = []
    enemies = []
    proj = []
    score = 0
    numeroNavin=0
    running = True

    arma1 = armaAtiva(0.5, 20, 21, 100, 1)
    arma2 = armaAtiva(0.0, 30, 10, 10, 1)
    arma3 = armaAtiva(2, 10, 70, 500, 1)

    armaAtual = arma1


    while running:      #LOOP DE RODAR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        

        #Teclas de movi do player
        keys = pygame.key.get_pressed()


        #troca de armas
        if keys[pygame.K_0]:
            armaAtual = arma1
        elif keys[pygame.K_9]:
            armaAtual = arma2
        elif keys[pygame.K_8]:
            armaAtual = arma3

        #movimento do player
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        player.move(dx, dy, player_speed)


        #Spawn de bullet
        keys = pygame.key.get_pressed()
        var = armaAtual.shoot(keys, player.rect.centerx, player.rect.top, bullets)
        if var is not None:
            bullets.append(var)

        #Movimento de bullet 
        armaAtual.bullet_movement(bullets)

        

        #Spawn de enemies
        if random.randint(1, 30000) == 1: 
            enemies.append(Enemy())

        #Movimento de enemies
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.top > HEIGHT:
                enemies.remove(enemy)
                score += 1 

        #Colisão de enemies com bullet
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 5  
                    break

        #Spawn nivan (NÃO TOQUE NESSA LIST)
        navins = []
        vida =[]
        if dano > 0:
            navins.append(NAVIN(numeroNavin%3, navinLista))
            vida.append(barraDeVida(3000-dano))
            #Spawn projetil
            if random.randint(1, 3) == 1:
                proj.append(Projetil(naturaisLista, WIDTH))

            #Movimento de projetil
            for projet in proj[:]:
                projet.move()
                if projet.rect.top > HEIGHT:
                    proj.remove(projet)
        elif dano<=0:   #apaga com os projeteis qnd navin morre
            proj=[]

        #Tick de animacao do navin
        if numeroNavin==30:
            numeroNavin=1
        elif numeroNavin==31:
            numeroNavin=2
        elif numeroNavin==32:
            numeroNavin=0


        #Colisão bullet com navin
        for bullet in bullets:
            for navin in navins:
                if bullet.rect.colliderect(navin.rect):
                    dano -= bullet.danoBala
                    bullets.remove(bullet)

        #Desenho player, fundo, bullet
        screen.blit(background, (0, 0))  #
        screen.blit(player.image, player.rect)  
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

        #Score (ADD VIDA, ARMA, VIDA NAVIN)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        #Tela de gameover (cogitar sistema de vida no lugar do hit kill)
        for projes in proj:
            if player.rect.colliderect(projes.rect):
                game_over_screen(running)

        #Comando pygame (NAO TOQUE)
        pygame.display.flip()
        numeroNavin+=3 #é 3 pq tem 4 imagens de navin
        clock.tick(30)

    #NAO TOQUE
    pygame.quit()

#NAO TOQUE
main()
