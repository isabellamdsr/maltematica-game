import pygame
import random
from moduloProjetil import Ability
from os.path import join
from os import walk
from moduloConfig import *

class Chefe(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_groups):
        super().__init__(sprite_groups)
        self.carregarImagens()
        self.sprite_groups = sprite_groups
        self.state, self.frame_index = 'idle', 0
        self.image = pygame.image.load(join('spritesGT', 'navin', 'idle', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        self.pos = pygame.Vector2(pos)
        self.direcaoNavin = pygame.Vector2(1, 0)
        self.velocidadeNavin = 2

        self.ataque_cooldown = 1500
        self.ultimo_ataque = pygame.time.get_ticks()

    def carregarImagens(self):
        self.frames = {'idle': [], 'ataque': []}

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('spritesGT', 'navin', state)):
                if file_names:
                    for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)


    def movement(self, tela_largura):
        if self.state == 'idle':
            self.rect.x += self.direcaoNavin.x * self.velocidadeNavin
            if self.rect.right > tela_largura or self.rect.left < 0:
                self.direcaoNavin *= -1

    def animation(self):

        self.frame_index += 0.2
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def attack(self):
        tempo_atual = pygame.time.get_ticks()

        if self.state == 'idle' and tempo_atual - self.ultimo_ataque >= 4000:
            self.state = 'ataque'
            self.original_rect = self.rect.copy()
            self.attack_start_time = tempo_atual

        if self.state == 'ataque':
            shake_offset = 5
            self.rect.x = self.original_rect.x + random.randint(-shake_offset, shake_offset)
            self.rect.y = self.original_rect.y + random.randint(-shake_offset, shake_offset)
            
            if tempo_atual - self.attack_start_time >= self.ataque_cooldown:
                self.state = 'idle'
                self.ultimo_ataque = tempo_atual
                self.rect = self.original_rect.copy()
                Ability.shoot(self.rect.midtop, self.sprite_groups)

    def update(self):
        self.animation()
        if fase_atual == 2:
            self.attack()
            self.movement(WIDTH)