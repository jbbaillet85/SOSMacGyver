#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Wall(pygame.sprite.Sprite):
    """Create walls for labyrinth"""
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./pictures/wall.jpg").pygame.Surface.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = SPRITE_TAILLE
        self.rect.x = SPRITE_TAILLE

def create_labyrinth():
    XX = 0
    YY = 0
    with open ("labyrinth.txt", "r") as file:
        for line in file:
            for sprite in line:
                if sprite == "M":
                    wall = Wall(XX, YY)
                    GROUP_WALLS.add(wall)
                    GROUP_GLOBAL_SPRITES.add(wall)
                XX += 1
            XX = 0
            YY +=1

if __name__ == "__wall__":
    Wall(self, x, y)