#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Wall(pygame.sprite.Sprite):
    """Create walls for labyrinth"""
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pictures/wall32.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_SIZE * y
        self.rect.x = SPRITE_SIZE * x
