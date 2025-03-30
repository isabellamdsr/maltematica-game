import pygame
from moduloBala import Bullet
import time

class armaAtiva():
    def __init__(self, atkSpeed, bulletSpeed, bulletSize, danoArma, qntBalas):
        self.qntBalas = qntBalas
        self.danoArma = danoArma
        self.bulletSpeed = bulletSpeed
        self.bulletSize = bulletSize
        self.cooldown = atkSpeed  #Em quantos milisecs a arma atira
        self.lastAtk = 0    #tempo do ultimo tiro com a arma


    def shoot(self,keys , playerX, playerY, bullets, arma):
            currentTime = time.time()
            anguloBala = [90, 75, 105, 60, 120]

            if keys[pygame.K_SPACE]:
                    if currentTime - self.lastAtk >= self.cooldown:     #se o tempo entre os tiros for maior que o 
                                                                        #cooldown a arma atira, e declara o tempo do
                        self.lastAtk = currentTime                      # ultimo tiro
                        for i in range(self.qntBalas):
                            bullets.append(Bullet(playerX, playerY, self.bulletSize, self.danoArma, anguloBala[i], arma))


    def bullet_movement(self,bullets):
        #Movimento de bullet
        

        for bullet in bullets[:]:
            bullet.move(self.bulletSpeed, bullet.anguloBala)
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

    def escolha(keys, arma1, arma2, arma3, arma4, armaAtual, arma):
        if keys[pygame.K_0]:
            armaAtual = arma1
            arma='arma1'
        elif keys[pygame.K_9]:
            armaAtual = arma2
            arma='arma2'
        elif keys[pygame.K_8]:
            armaAtual = arma3
            arma='arma3'
        elif keys[pygame.K_7]:
            armaAtual = arma4
            arma='arma4'
        else:
            arma=arma
            armaAtual=armaAtual
        return arma, armaAtual