#Imports
import time
import pygame
import random
from moduloConfig import *
from moduloPlayer import Player, vidaPlayer
from moduloBarraDeVida import barraDeVida, healthBar
from moduloNAVIN import Chefe
from moduloProjetil import Projetil, Vazio, Ability, Irra
from moduloArmaAtiva import armaAtiva
from moduloDesenho import *
from moduloColetaveis import *

#tela de gameover (sera completamente alterado quando o sprite de tela de gameover for inserido)
def game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta):
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
                    fase3(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                    return

def fase3(inventorioArmas, pistola, metralhadora, bazuca, escopeta):
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_3.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    navin = Chefe((720, 150), all_sprites)      #Classe do navin
    player = Player(player_size2, player_size, WIDTH, HEIGHT)   #Classe player
    vidaNavin = 7000      #vida do navin
    health_bar = healthBar() # Load da barra de vida
    fase_atual.append(3) # Criei a lista fase_atual dentro do Config
    
    #Lista de objetos moviveis gerados
    bullets = []
    proj = []
    vazio=[]
    irra = []

    running = True
    lastDmg = 0

    vidaJogador = vidaPlayer()      #Estabelece vida inicial do jogador
    vidaJogador.adicionarCoracao(3)

    armaAtual = pistola        #Definições de armas (atuais e equipadas)
    arma = 'pistola'

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
        if vidaNavin > 0:    
            vida.append(barraDeVida(7000-vidaNavin, 7000))

            #Lista com blocos de colisão (usados para a funcionalidade do projetil 3)
            listaBlocos = [(pygame.Rect(0, 0, 165, 810)),
                    (pygame.Rect(150, 0, 1140, 380)),
                    (pygame.Rect(1270, 0, 300, 810)),
                    (pygame.Rect(150, 790, 490, 100)),
                    (pygame.Rect(820, 790, 495, 90)),
                    (pygame.Rect(610, 375, 220, 170)),
                    (pygame.Rect(610, 670, 220, 170)),
                    (pygame.Rect(-1, -1, 1440, 1)),
                    (pygame.Rect(0, 811, 1440, 1))]

            randomico=random.randint(1, 30)

            #Spawn projetil 1
            if random.randint(1, 5) == 1:
                proj.append(Projetil(naturaisLista, WIDTH))

            #Spawn projetil 2
            if randomico == 1 and len(vazio)<1:
                tickSpawnVazio=pygame.time.get_ticks()
                a=random.randint(1200, 2000)
                vazio.append(Vazio(WIDTH))

            #Spawn projetil 3
            if  randomico == 2 and len(irra)<1:
                tickSpawnIrra=pygame.time.get_ticks()
                aleatorio=random.randint(1200, 2000)
                irra.append(Irra(WIDTH))

            #Movimento de projetil 1
            for projet in proj[:]:
                projet.move()
                if projet.rect.y > HEIGHT:
                    proj.remove(projet)

            #Movimento de projetil 2
            for projV in vazio:
                projV.printar(vazio)
                expX=vazio[-1].rect.x-90
                expY=vazio[-1].rect.y-90
                projV.moveVazio(tickSpawnVazio, a)
                if pygame.time.get_ticks() >= tickSpawnVazio+(a):
                    explosao=pygame.Rect(expX, expY, 200, 200)
                    screen.blit(pygame.transform.scale((pygame.image.load('spritesGT/Explosao.png')), (200, 200)), explosao)
                    if pygame.time.get_ticks()>tickSpawnVazio+(a)+300:
                        if explosao.colliderect(player):
                            if len(vidaJogador.vida) > 1:
                                vidaJogador.retirarCoracao(1)
                            else:    
                                game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                        vazio.remove(projV)

            #Movimento de projetil 3
            for projI in irra:
                listaBlocos.append(projI.rect)
                projI.printar(irra)
                projI.moveIrra(tickSpawnIrra, aleatorio, player)
                if pygame.time.get_ticks() >= tickSpawnIrra+(aleatorio)+3000:
                    if projI.rect.colliderect(player):
                        if len(vidaJogador.vida) > 1:
                            vidaJogador.retirarCoracao(1)
                        else:    
                            game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                    irra.remove(projI)

            #Colisão bullet com navin
            for bullet in bullets:
                if bullet.rect.colliderect(navin.rect):
                    vidaNavin -= bullet.danoBala
                    bullets.remove(bullet)

            all_sprites.update()
            all_sprites.draw(screen)

        elif vidaNavin<=0:   #apaga com os projeteis qnd navin morre
            proj=[]
            vazio=[]
            irra=[]
            navin.kill()    #Apago de sprites
            listaBlocos = [(pygame.Rect(0, 0, 165, 810)),    #Lista de blocos após a derrota de navin
                    (pygame.Rect(150, 0, 1140, 380)),
                    (pygame.Rect(1270, 0, 300, 810)),
                    (pygame.Rect(150, 790, 490, 100)),
                    (pygame.Rect(820, 790, 495, 90)),
                    (pygame.Rect(610, 375, 220, 170)),
                    (pygame.Rect(610, 670, 220, 170)),
                    (pygame.Rect(-1, -1, 1440, 1)),
                    (pygame.Rect(0, 811, 1440, 1))]

        #Desenhos
        printar=desenhar(screen, RED, bullets, proj, vida, player, vidaJogador.vida)
        printar        
        if vidaNavin>0:
            health_bar.printar(screen) # Blit da barra de vida
        
        #troca de armas
        arma, armaAtual=armaAtiva.escolha(keys, pistola, metralhadora, bazuca, escopeta, armaAtual, arma, inventorioArmas)
        printColetaveis(inventorioArmas, pistola, metralhadora, bazuca, escopeta)

        currentTime = time.time()

        for projes in proj:
            if player.rect.colliderect(projes.rect):
                if currentTime - lastDmg > 0.5:
                    if len(vidaJogador.vida) > 1:
                        vidaJogador.retirarCoracao(1)
                    else:    
                        game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                    lastDmg = currentTime

        for attack in all_sprites: # Pega todos os sprites com a instância 'Ability'
            if isinstance(attack, Ability): 
                if player.rect.colliderect(attack.rect) and vidaNavin > 0: # Colisão do ataque em cone como player
                    if currentTime - lastDmg > 5: # Intervalo o suficiente para que o jogador não leve dano de projéteis consecutivos dentro do ataque
                            if len(vidaJogador.vida) > 1:
                                vidaJogador.retirarCoracao(1)
                            else:    
                                game_over_screen(running)
                            lastDmg = currentTime

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
