import pygame
import time
from moduloCoracao import coracao

class vidaPlayer():
    def __init__(self):
        self.vida = []
        self.xAtual = 1300
        self.yAtual = 100


    def adicionarCoracao(self, qntCoracoes):
        for i in range(qntCoracoes):
            self.vida.append(coracao(self.xAtual, self.yAtual))
            self.xAtual -= 60
        

    def retirarCoracao(self, qntCoracoes):
            for i in range(qntCoracoes):
                self.vida.pop()