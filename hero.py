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
        self.rect.y = 0
        self.rect.x = 0
        self.position = (self.rect.x, self.rect.y)
    
    def move(self, direction, position_empty):
        """methode move for Hero"""
        if direction == "L":
            if self.rect.x >0:
                self.rect.x -= SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
        elif direction == "R":
            if self.rect.x < SPRITE_SIZE*(SPRITE_NUMBER-1):
                self.rect.x += SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
        elif direction == "U":
            if self.rect.y <0:
                self.rect.y -= SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
        elif direction == "D":
            if self.rect.y < SPRITE_SIZE*(SPRITE_NUMBER-1):
                self.rect.y += SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
        return self.position
    
    def blit(self):
        BACKGROUND.blit(self.image,(self.position))
        