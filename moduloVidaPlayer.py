import pygame
import time
from moduloCoracao import coracao

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