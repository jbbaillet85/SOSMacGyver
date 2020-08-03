#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Hero(pygame.sprite.Sprite):
    """Create hero for labyrinth"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pictures/MacGyver32.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_SIZE*y
        self.rect.x = SPRITE_SIZE*x
    
    