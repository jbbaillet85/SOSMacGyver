#! /usr/bin/env python3
#coding utf-8

import pygame
import random
from constants import *

class Items(pygame.sprite.Sprite):
    """Create items for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, SPRITE_NUMBER-1)*SPRITE_SIZE
        self.rect.x = random.randint(0, SPRITE_NUMBER-1)*SPRITE_SIZE