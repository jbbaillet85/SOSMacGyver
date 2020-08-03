#! /usr/bin/env python3
#coding utf-8

import pygame
import constants
import random

class Items(pygame.sprite.Sprite):
    """Create items for labyrinth"""
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pictures/ether32.jpg")
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, SPRITE_NUMBER-1)*SPRITE_SIZE
        self.rect.x = random.randint(0, SPRITE_NUMBER-1)*SPRITE_SIZE
