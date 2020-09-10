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
        self.Y_LOGIQUE = 0
        self.X_LOGIQUE = 0
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_LOGIQUE * SPRITE_SIZE
        self.rect.x = self.X_LOGIQUE * SPRITE_SIZE
        self.position = (self.rect.x, self.rect.y)
        self.direction = "direction"
    
    def move(self, direction):
        if direction == "L":
            self.position = ((self.rect.x-SPRITE_SIZE), self.rect.y)
        elif direction == "R":
            self.position = ((self.rect.x+SPRITE_SIZE), self.rect.y)
        elif direction == "U":
            self.position = (self.rect.x, (self.rect.y-SPRITE_SIZE))
        elif direction == "D":
            self.position = (self.rect.x, (self.rect.y+SPRITE_SIZE))