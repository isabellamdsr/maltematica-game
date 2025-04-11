import pygame
from moduloConfig import *
from fase1 import fase1


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.pos = pygame.Vector2(pos)
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        self.text_rect = self.text.get_rect(center=(self.pos.x, self.pos.y))

        self.hover_sound = pygame.mixer.Sound('sons/trocaBotao.wav') # Pretendo usar isso depois

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

        if hasattr(self, 'chave_esquerda') and self.chave_esquerda is not None:
            screen.blit(self.chave_esquerda, self.chave_esquerda_rect)
    
        if hasattr(self, 'chave_direita') and self.chave_direita is not None:
            screen.blit(self.chave_direita, self.chave_direita_rect)
    
    def checkForInput(self, pos):
        if (self.rect.left <= pos[0] < self.rect.right and
            self.rect.top <= pos[1] < self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            return True
        return False
                                                                                 
    def changeColor(self, pos):
        if (self.rect.left <= pos[0] < self.rect.right and
            self.rect.top <= pos[1] < self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            self.chave_esquerda = self.font.render("{", False, self.hovering_color)
            self.chave_esquerda_rect = self.chave_esquerda.get_rect()
            self.chave_esquerda_rect.right = self.text_rect.left - 5
            self.chave_esquerda_rect.centery = self.text_rect.centery - 5
            
            self.chave_direita = self.font.render("}", False, self.hovering_color)
            self.chave_direita_rect = self.chave_direita.get_rect()
            self.chave_direita_rect.left = self.text_rect.right + 5
            self.chave_direita_rect.centery = self.text_rect.centery - 5
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.chave_esquerda = None
            self.chave_direita = None 

def get_font(size, font_file):
    return pygame.font.Font(font_file, size)

def historiaInicio():
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
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.rewind()
                    pygame.mixer.music.unpause()
                    fase1()
                    return
        pygame.display.flip()

def controls():
    while True:
        pygame.display.set_caption('Menu')
        screen.blit(background_inicial, (0, 0))
        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()

        CONTROLS_TEXT = get_font(80, 'fonts/fontezinha.otf').render("Controles do jogo", True, "White")
        OPTIONS_TEXT_RECT = CONTROLS_TEXT.get_rect(center=(WIDTH / 2, 100))
        CONTROLS_IMG = pygame.image.load("spritesGT/controls.png")
        screen.blit(CONTROLS_IMG, (350,183))

        controls_texts = [CONTROLS_TEXT]
        controls_rects = [OPTIONS_TEXT_RECT]

        # This pairs each text with its corresponding rect
        for i in range(len(controls_texts)):
            screen.blit(controls_texts[i], controls_rects[i])

        CONTROLS_BACK = Button(image=None, pos=(WIDTH / 2, 700), 
                            text_input="BACK", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="White")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                    main_menu()

        pygame.display.flip()



def play():
    historiaInicio()


def main_menu():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Menu')  
     
    done = False

    clock = pygame.time.Clock()

    while not done:
        screen.blit(background_inicial, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()

        mal_text = get_font(200, 'fonts/Chalk Board.ttf').render("MAL", True, "Red")
        mal_rect = mal_text.get_rect()
        tematica_text = get_font(200, 'fonts/Chalk Board.ttf').render("TEMÁTICA", True, "White")
        tematica_rect = tematica_text.get_rect()

        mal_rect.topright = (WIDTH / 2 - tematica_rect.width / 4 , 175 - mal_rect.height / 2)
        tematica_rect.topleft = (mal_rect.right, mal_rect.top)

        screen.blit(mal_text, mal_rect)
        screen.blit(tematica_text, tematica_rect)


        PLAY = Button(image=None, pos=(WIDTH / 2, 340), 
                                text_input="START GAME", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="White")
        
        CONTROLS = Button(image=None, pos=(WIDTH / 2, 460), 
                                text_input="CONTROLS", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="White")
        
        QUIT = Button(image=None, pos=(WIDTH / 2, 580), 
                                text_input="QUIT", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="White")
        

        for button in [PLAY, CONTROLS, QUIT]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY.checkForInput(menu_mouse_pos):
                    done = True
                    play()
                if CONTROLS.checkForInput(menu_mouse_pos):
                    done = True
                    controls()
                if QUIT.checkForInput(menu_mouse_pos):
                    done = True
                    pygame.quit()

        pygame.display.flip()

        