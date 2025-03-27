import pygame
import random

#enemy class
class Enemy:
    def __init__(self, WIDTH, enemy_size):
        self.rect = pygame.Rect(random.randint(0, WIDTH - enemy_size), 0, enemy_size, enemy_size)

    def move(self, enemy_speed):
        self.rect.y += enemy_speed #emeny cai pro inferno