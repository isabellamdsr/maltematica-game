import pygame

#Comando pygame (NAO TOQUE)
pygame.init()

#Fontes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

fase_atual = [] # Adicionei para gerenciar as mecânicas do Navin, em cada fase nova dá append com o número da fase

#Tela inicial
background_inicial = pygame.image.load('spritesGT/Background_Inicial.png')

#Musica
pygame.mixer.music.load("soundtrack/SoundtrackJogo.mpga")
pygame.mixer.music.play(loops=-1)

#Tela 
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")


#Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Sprites
   # Naturais
naturaisLista=['spritesGT/Naturais/zero.png','spritesGT/Naturais/um.webp','spritesGT/Naturais/dois.png',
               'spritesGT/Naturais/tres.png','spritesGT/Naturais/quatro.png','spritesGT/Naturais/cinco.png',
               'spritesGT/Naturais/seis.png','spritesGT/Naturais/sete.png','spritesGT/Naturais/oito.png',
               'spritesGT/Naturais/nove.png']

   # Animação Navin
navinLista=['spritesGT/navin/navin_idle.png','spritesGT/navin/navin_idle2.png','spritesGT/navin/navin_idle3.png','spritesGT/navin/navin_idle4.png']

#Configs Gerais

#player config
player_size = 66
player_size2 = 60
player_speed = 10

#bullet config
bullet_size = 21
bullet_speed = 20

#enemy config
enemy_size = 50
enemy_speed = 2

#projetil config
projetil_size = 20
projetil_speed = 12