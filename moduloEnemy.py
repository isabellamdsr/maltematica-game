import pygame
import random

#enemy class
class Enemy:
    def __init__(self, WIDTH, enemy_size):
        self.rect = pygame.Rect(random.randint(0, WIDTH - enemy_size), 0, enemy_size, enemy_size)

    def move(self, enemy_speed):
        self.rect.y += enemy_speed #emeny cai pro inferno


        '''
        #Spawn de enemies
        if random.randint(1, 30000) == 1: 
            enemies.append(Enemy())

        #Movimento de enemies
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.top > HEIGHT:
                enemies.remove(enemy)
                score += 1 

        #Colisão de enemies com bullet
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 5  
                    break
        '''