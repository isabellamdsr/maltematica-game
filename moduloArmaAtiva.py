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


    def shoot(self,keys , playerX, playerY, bullets):
            currentTime = time.time()
            if keys[pygame.K_SPACE]:
                if currentTime - self.lastAtk >= self.cooldown:     #se o tempo entre os tiros for maior que o 
                                                                    #cooldown a arma atira, e declara o tempo do
                    self.lastAtk = currentTime                      # ultimo tiro
                    bullets.append(Bullet(playerX, playerY, self.bulletSize, self.danoArma))

    def bullet_movement(self,bullets):
        #Movimento de bullet

        for bullet in bullets[:]:
            bullet.move(self.bulletSpeed, 90)
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)