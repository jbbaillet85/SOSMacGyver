#! /usr/bin/env python3
#coding utf-8

import pygame

GROUP_WALLS = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
    """Create walls for labyrinth"""
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pictures/wall.jpg").pygame.Surface.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 30
        self.rect.x = 30

def create_labyrinth():
    XX = 0
    YY = 0
    with open ("labyrinth.txt", "r") as file:
        for line in file:
            for sprite in line:
                if sprite == "M":
                    mur = Mur(XX, YY)
                    GROUP_WALLS.add(mur)
                XX += 1
            XX = 0
            YY +=1

wall = Wall(30,30)
create_labyrinth

if __name__ == "__wall__":
    Wall(self, x, y)