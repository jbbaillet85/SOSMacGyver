#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Hero(pygame.sprite.Sprite):
    """Create hero for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_SIZE
        self.rect.x = SPRITE_SIZE