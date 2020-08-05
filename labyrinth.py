#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *

class Labyrinth(pygame.sprite.Sprite):
    """Create labyrinth for game"""
    def __init__(self, wall, arrival, labyrinth):
        pygame.sprite.Sprite.__init__(self)
        self.wall = pygame.image.load(wall)
        self.arrival = pygame.image.load(arrival)
        self.labyrinth = labyrinth

    def create_labyrinth():
        num_line = 0
        with open(labyrinth, "r") as file:
            for line in file:
                num_box = 0
                for sprite in line:
                    x = num_box*SPRITE_SIZE
                    y = num_line*SPRITE_SIZE
                    if sprite == "W":
                        background.blit(wall,(x, y))
                    elif sprite == "A":
                        background.blit(arrival,(x,y))
                    num_box += 1
                num_line += 1

labyrinth = Labyrinth("pictures/wall32.jpg", "pictures/Gardien32.png", "labyrinth")
labyrinth.create_labyrinth("labyrinth.txt")