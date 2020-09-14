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
    
    def move(self, direction):
        """methode move for Hero"""
        if direction == "L":
            if self.position in LIST_EMPTY_POSITIONS:
                self.position = ((self.rect.x-SPRITE_SIZE), self.rect.y)
        elif direction == "R":
            self.position = ((self.rect.x+SPRITE_SIZE), self.rect.y)
        elif direction == "U":
            self.position = (self.rect.x, (self.rect.y-SPRITE_SIZE))
        elif direction == "D":
            self.position = (self.rect.x, (self.rect.y+SPRITE_SIZE))
        return BACKGROUND.blit(self.image, (self.position))
    
    def exit(self, arrival):
        """methode for win"""
        if self.position == arrival:
            print("C'est gagné")
            pygame.quit()