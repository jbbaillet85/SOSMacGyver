#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Gardian(pygame.sprite.Sprite):
    """Create gardian for labyrinth"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.load.image("pictures/Gardien32.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_SIZE*y
        self.rect.x = SPRITE_SIZE*x