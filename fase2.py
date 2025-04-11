#Imports
import time
import pygame
import random
from moduloConfig import *
from moduloPlayer import Player, vidaPlayer
from moduloBarraDeVida import barraDeVida, healthBar
from moduloNAVIN import Chefe
from moduloProjetil import Projetil, Vazio, Ability
from moduloArmaAtiva import armaAtiva
from moduloDesenho import *
from moduloColetaveis import *
from fase3 import fase3
from moduloBarraDeVida import nome

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
                    fase2(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                    return

def fase2(inventorioArmas, pistola, metralhadora, bazuca, escopeta):
    # Carregar a imagem de fundo
    background = pygame.image.load("spritesGT/Map_2.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar o tamanho da imagem do fundo

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    navin = Chefe((720, 150), all_sprites)  #Classe do navin
    player = Player(player_size2, player_size, WIDTH, HEIGHT)   #Classe player
    vidaNavin = 5000      #vida do navin
    health_bar = healthBar() # Load da barra de vida
    fase_atual.append(2) # Criei a lista fase_atual dentro do Config
    
    #Lista de objetos moviveis gerados
    bullets = []
    proj = []
    vazio=[]

    running = True
    lastDmg = 0

    vidaJogador = vidaPlayer()      #Estabelece vida inicial do jogador
    vidaJogador.adicionarCoracao(3)

    armaAtual = pistola        #Definições de armas (atuais, equipadas e coletaveis)
    arma = 'pistola'
    proxArma1 = Bazuca()
    proxArma = Shotgun()

    listaBlocos = [(pygame.Rect(0, 0, 241, 810)),        #Lista com blocos de colisão
    (pygame.Rect(150, 0, 1140, 292)),
    (pygame.Rect(1210, 0, 300, 810)),
    (pygame.Rect(150, 720, 490, 292)),
    (pygame.Rect(820, 720, 495, 90)),
    (pygame.Rect(150, 1101, 165, 90)),
    (pygame.Rect(518, 292, 413, 257)),
    (pygame.Rect(-1, -1, 1440, 1)),
    (pygame.Rect(0, 811, 1440, 1))]


    while running:      #LOOP DE RODAR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.blit(background, (0, 0))  #background

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
            vida.append(barraDeVida(5000-vidaNavin, 5000))

            #Spawn projetil 1
            if random.randint(1, 5) == 1:
                proj.append(Projetil(naturaisLista, WIDTH))

            #Spawn projetil 2
            if random.randint(1, 30) == 1 and len(vazio)<1:
                tickSpawnVazio=pygame.time.get_ticks()
                a=random.randint(1200, 2000)
                vazio.append(Vazio(WIDTH))

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

            all_sprites.update()
            all_sprites.draw(screen)

            #Colisão bullet com navin
            for bullet in bullets:
                if bullet.rect.colliderect(navin.rect):
                    vidaNavin -= bullet.danoBala
                    bullets.remove(bullet)

        elif vidaNavin<=0:   
            #apaga com os projeteis qnd navin morre
            proj=[]
            vazio=[]
            navin.attacks = []
            navin.kill()    #Apago de sprites
            listaBlocos = [(pygame.Rect(0, 0, 241, 810)),   #Lista de blocos após a derrota de navin
                        (pygame.Rect(150, 0, 500, 292)),
                        (pygame.Rect(795, 0, 495, 292)),
                        (pygame.Rect(1210, 0, 300, 810)),
                        (pygame.Rect(150, 720, 490, 292)),
                        (pygame.Rect(820, 720, 495, 90)),
                        (pygame.Rect(150, 1101, 165, 90)),
                        (pygame.Rect(518, 292, 132, 257)),
                        (pygame.Rect(795, 292, 136, 257)),
                        (pygame.Rect(-1, 60, 1440, 1)),
                        (pygame.Rect(0, 811, 1440, 1)),
                        ]
            
            #Funções para drop e coleta de armas
            proxArma.coleta(player, inventorioArmas, escopeta) 
            proxArma1.coleta(player, inventorioArmas, bazuca)

            if player.rect.x>650 and player.rect.y<90:      #Ida para a fase 3
                fase3(inventorioArmas, pistola, metralhadora, bazuca, escopeta)

        #Desenho player, fundo, bullet
        printar=desenhar(screen, RED, bullets, proj, vida, player, vidaJogador.vida)
        printar        
        if vidaNavin>0:
            screen.blit(nome().image, nome().rect)      
            health_bar.printar(screen) # Blit da barra de vida
        
        #troca de armas
        arma, armaAtual=armaAtiva.escolha(keys, pistola, metralhadora, bazuca, escopeta, armaAtual, arma, inventorioArmas)
        printColetaveis(inventorioArmas, pistola, metralhadora, bazuca, escopeta)

        currentTime = time.time()

        #Codigo par atirar
        for projes in proj:
            if player.rect.colliderect(projes.rect):
                if currentTime - lastDmg > 0.5:
                    if len(vidaJogador.vida) > 1:
                        vidaJogador.retirarCoracao(1)
                    else:    
                        game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                    lastDmg = currentTime
                    proj.remove(projes)

        for attack in all_sprites: # Pega todos os sprites com a instância 'Ability'
            if isinstance(attack, Ability): 
                if player.rect.colliderect(attack.rect) and vidaNavin > 0: # Colisão do ataque em cone como player
                    if currentTime - lastDmg > 5: # Intervalo o suficiente para que o jogador não leve dano de projéteis consecutivos dentro do ataque
                            if len(vidaJogador.vida) > 1:
                                vidaJogador.retirarCoracao(1)
                            else:    
                                game_over_screen(inventorioArmas, pistola, metralhadora, bazuca, escopeta)
                            lastDmg = currentTime

        #Comando pygame
        pygame.display.flip()
        clock.tick(30)

        all_sprites.update() # Talvez eu deva mudar o nome pra some_sprites... já que só tem os que eu fiz
        all_sprites.draw(screen)
        
    pygame.quit()
