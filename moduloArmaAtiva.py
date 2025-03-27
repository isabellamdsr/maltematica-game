import pygame
from moduloBala import Bullet
import time

class armaAtiva():
    def __init__(self, atkSpeed, bulletSpeed, bulletSize):
        self.bulletSpeed = bulletSpeed
        self.bulletSize = bulletSize
        self.cooldown = atkSpeed  #atk speed é em quantos milisecs a arma atira
        self.lastAtk = 0


    def shoot(self,keys , playerX, playerY, bullets):
            currentTime = time.time()
            if keys[pygame.K_SPACE]:
                print(currentTime)
                if currentTime - self.lastAtk >= self.cooldown:
                    self.lastAtk = currentTime
                    bullets.append(Bullet(playerX, playerY, self.bulletSize))

    def bullet_movement(self,bullets):
        #Movimento de bullet
        for bullet in bullets[:]:
            bullet.move(self.bulletSpeed)
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)