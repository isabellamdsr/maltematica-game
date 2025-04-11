#Imports
import time
import pygame
import random
from moduloConfig import *
from moduloPlayer import Player, vidaPlayer
from moduloBarraDeVida import barraDeVida, healthBar
from moduloNAVIN import Chefe
from moduloProjetil import Projetil, Ability
from moduloArmaAtiva import armaAtiva
from moduloDesenho import *
from moduloColetaveis import *
from fase2 import fase2

pygame.mixer.Channel(1)#channel da musica
pygame.mixer.Channel(4)#channel dos efeitos sonoros

#tela de gameover (sera completamente alterado quando o sprite de tela de gameover for inserido)
def game_over_screen(rodando):
    pygame.mixer.music.pause()
    gameOverSfx = pygame.mixer.Sound("sons/gameOver.mp3")
    pygame.mixer.Channel(4).play(gameOverSfx)
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
    while True: # Loop da tela de gamevoer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.unpause()
                    fase1()
                    return
                
# Main game loop
def fase1():
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_1.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    navin = Chefe((720, 150), all_sprites)
    player = Player(player_size2, player_size, WIDTH, HEIGHT)
    vidaNavin = 3000       #vida do navin
    health_bar = healthBar() # Load da barra de vida
    fase_atual.append(1)
    
    #Lista de objetos moviveis gerados nessa fase
    bullets = []
    proj = []
    vazio=[]
    running = True
    lastDmg = 0

    vidaJogador = vidaPlayer()      #Estabelece vida inicial do jogador
    vidaJogador.adicionarCoracao(3)

    pistola = armaAtiva(0.5, 20, 21, 10000, 1)        #Estabelece parametros das armas
    metralhadora = armaAtiva(0.0, 30, 10, 10, 1)
    bazuca = armaAtiva(2, 10, 70, 500, 1)
    escopeta = armaAtiva(0.5,20, 15, 70, 5)

    armaAtual = pistola         #Definições de armas (atuais, equipadas e coletaveis)
    arma = 'pistola'
    inventorioArmas = [pistola]
    proxArma = Metralhadora()

    listaBlocos = [(pygame.Rect(0, 0, 150, 810)),       #Lista com blocos de colisão
    (pygame.Rect(150, 0, 1140, 292)),
    (pygame.Rect(1290, 0, 150, 810)),
    (pygame.Rect(150, 744, 495, 292)),
    (pygame.Rect(150, 1101, 165, 66)),
    (pygame.Rect(795, 744, 495, 66)),
    (pygame.Rect(-1, -1, 1440, 1)),
    (pygame.Rect(0, 811, 1440, 1))]


    while running:      #LOOP DE RODAR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.blit(background, (0, 0))  #
        #screen.blit(player.image, player.rect)  # Comentei pra dar o blit do player na função desenhar e não aqui. Apenas explicando se causar algum erro

        #movimento do player
        keys = pygame.key.get_pressed()        #Teclas de movi do player
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        player.move(dx, dy, player_speed, listaBlocos)

        #Spawn de bullet
        keys = pygame.key.get_pressed()
        var = armaAtual.shoot(keys, player.rect.centerx, player.rect.top, bullets, arma)
        if var is not None:
            bullets.append(var)

        #Movimento de bullet 
        armaAtual.bullet_movement(bullets)

        #Spawn nivan
        vida =[]
        if vidaNavin > 0:       #Condicional para navin vivo
            vida.append(barraDeVida(3000-vidaNavin, 3000))

            #Spawn projetil 1
            if random.randint(1, 5) == 1:
                proj.append(Projetil(naturaisLista, WIDTH))

            #Movimento de projetil 1
            for projet in proj[:]:
                projet.move()
                if projet.rect.y > HEIGHT:
                    proj.remove(projet)

            #Colisão bullet com navin
            for bullet in bullets:
                if bullet.rect.colliderect(navin.rect):
                    vidaNavin -= bullet.danoBala
                    bullets.remove(bullet)

            all_sprites.update()
            all_sprites.draw(screen)

        elif vidaNavin<=0:  #Condicional de navin derrotado
            #apaga com os projeteis qnd navin morre
            proj=[]
            vazio=[]
            navin.kill()
            listaBlocos = [(pygame.Rect(0, 0, 150, 810)),   #Lista de blocos de colisão após navin morrer
                    (pygame.Rect(150, 0, 495, 292)),
                    (pygame.Rect(795, 0, 495, 292)),
                    (pygame.Rect(150, 744, 495, 292)),
                    (pygame.Rect(1290, 0, 150, 810)),
                    (pygame.Rect(150, 1101, 165, 66)),
                    (pygame.Rect(795, 744, 495, 66)),
                    (pygame.Rect(-1, -1, 1440, 1)),
                    (pygame.Rect(0, 811, 1440, 1))
                    ]
            if player.rect.x>650 and player.rect.y<40:      #Ida para fase2
                   fase2(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
            proxArma.coleta(player, inventorioArmas, metralhadora)
    


        #Desenho player, fundo, bullet
        printar=desenhar(screen, RED, bullets, proj, vida, player, vidaJogador.vida)  #classe de desenhos
        printar
        if vidaNavin>0:
            health_bar.printar(screen) # Blit da barra de vida
        
        #troca de armas
        arma, armaAtual=armaAtiva.escolha(keys, pistola, metralhadora, bazuca, escopeta, armaAtual, arma, inventorioArmas)
        printColetaveis(inventorioArmas, pistola, metralhadora, bazuca, escopeta)

        currentTime = time.time()

        #Codigo para Atirar 
        for projes in proj:
            if player.rect.colliderect(projes.rect):
                if currentTime - lastDmg > 0.5:
                    if len(vidaJogador.vida) > 1:
                        vidaJogador.retirarCoracao(1)
                    else:    
                        game_over_screen(running)
                    lastDmg = currentTime

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()