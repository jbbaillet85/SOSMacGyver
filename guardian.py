#! /usr/bin/env python3
#coding utf-8

import pygame

from constants import *

class Gardian(pygame.sprite.Sprite):
    """Create gardian for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_SIZE*SPRITE_NUMBER
        self.rect.x = SPRITE_SIZE*SPRITE_NUMBER