import pygame
from moduloBotao import Button
from moduloConfig import *
from fase1 import fase1

def get_font(size, font_file):
    return pygame.font.Font(font_file, size)

def help():
    while True:
        pygame.display.set_caption('Menu')
        screen.blit(background_inicial, (0, 0))
        HELP_MOUSE_POS = pygame.mouse.get_pos()

        HELP_TEXT = get_font(40, 'fonts/fontezinha.otf').render("seria bom uma tela explicando como joga o jogo", True, "White")
        HELP_TEXT_RECT = HELP_TEXT.get_frect(center=(WIDTH / 2, 200))
        screen.blit(HELP_TEXT, HELP_TEXT_RECT)

        HELP_BACK = Button(image=None, pos=(WIDTH / 2, 400), 
                            text_input="BACK", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        
        HELP_BACK.changeColor(HELP_MOUSE_POS)
        HELP_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(HELP_MOUSE_POS):
                    main_menu()


        pygame.display.flip()

def options():
    while True:
        pygame.display.set_caption('Menu')
        screen.blit(background_inicial, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(40, 'fonts/fontezinha.otf').render("aqui só consigo pensar em opções de som?", True, "White")
        OPTIONS_TEXT_2 = get_font(40, 'fonts/fontezinha.otf').render("um slider geral/master, um pra efeitos sonoros e outro pra música", True, "White")
        OPTIONS_TEXT_3 = get_font(40, 'fonts/fontezinha.otf').render("tem vídeo de 10 minutos no yt explicando como faz slider no pygame", True, "White")
        OPTIONS_TEXT_4 = get_font(40, 'fonts/fontezinha.otf').render("talvez uma pra mudar resolução da tela mas pode ser ambicioso", True, "White")
        OPTIONS_TEXT_RECT = OPTIONS_TEXT.get_frect(center=(WIDTH / 2, 200))
        OPTIONS_TEXT_RECT_2 = OPTIONS_TEXT_2.get_frect(center=(WIDTH / 2, 300))
        OPTIONS_TEXT_RECT_3 = OPTIONS_TEXT_3.get_frect(center=(WIDTH / 2, 400))
        OPTIONS_TEXT_RECT_4 = OPTIONS_TEXT_4.get_frect(center=(WIDTH / 2, 500))

        option_texts = [OPTIONS_TEXT, OPTIONS_TEXT_2, OPTIONS_TEXT_3, OPTIONS_TEXT_4]
        option_rects = [OPTIONS_TEXT_RECT, OPTIONS_TEXT_RECT_2, OPTIONS_TEXT_RECT_3, OPTIONS_TEXT_RECT_4]

        # This pairs each text with its corresponding rect
        for i in range(len(option_texts)):
            screen.blit(option_texts[i], option_rects[i])

        OPTIONS_BACK = Button(image=None, pos=(WIDTH / 2, 700), 
                            text_input="BACK", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.flip()

def play():
    fase1()


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
                                text_input="START GAME", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        
        OPTIONS = Button(image=None, pos=(WIDTH / 2, 460), 
                                text_input="OPTIONS", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        
        HELP = Button(image=None, pos=(WIDTH / 2, 580), 
                                text_input="HELP", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        
        QUIT = Button(image=None, pos=(WIDTH / 2, 700), 
                                text_input="QUIT", font=get_font(75, 'fonts/fontezinha.otf'), base_color="White", hovering_color="Green")
        

        for button in [PLAY, OPTIONS, HELP, QUIT]:
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
                if OPTIONS.checkForInput(menu_mouse_pos):
                    done = True
                    options()
                if HELP.checkForInput(menu_mouse_pos):
                    done = True
                    help()
                if QUIT.checkForInput(menu_mouse_pos):
                    done = True
                    pygame.quit()

        pygame.display.flip()