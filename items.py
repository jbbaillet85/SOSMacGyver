#! /usr/bin/env python3
#coding utf-8

import random

import pygame

from constants import *

class Items(pygame.sprite.Sprite):
    """Create items for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path)
        self.name = name
        self.X_LOGIQUE = random.randint(0, SPRITE_NUMBER-1)
        self.Y_LOGIQUE = random.randint(0, SPRITE_NUMBER-1)
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_LOGIQUE * SPRITE_SIZE
        self.rect.x = self.X_LOGIQUE*SPRITE_SIZE
        self.position = (self.rect.y, self.rect.x)