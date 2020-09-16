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
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.position = (self.rect.y, self.rect.x)

    def placement_item(self, position_empty):
        BACKGROUND.blit(self.image, random.choice(position_empty))
