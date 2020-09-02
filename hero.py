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
        self.direction = "0"
    
    def move(self):
        x_current = self.rect.x
        y_current = self.rect.y
        if self.move == "L":
            self.rect.x -= SPRITE_SIZE
            self.direction = "0"
        elif self.move == "R":
            self.rect.x += SPRITE_SIZE
            self.direction = "0"
        elif self.move == "U":
            self.rect.y -= SPRITE_SIZE
            self.direction = "0"
        elif self.move == "D":
            self.rect.y += SPRITE_SIZE
            self.direction = "0"
        
        liste_collision_wall = pygame.sprite.spritecollide(self, GROUP_WALLS, False)
        if len(liste_collision_wall)>0:
            self.rect.x = x_current
            self.rect.y = y_current
        
        liste_collision_items = pygame.sprite.spritecollide(self, GROUP_ITEMS, False)
        for items in liste_collision_items:
            items.kill()