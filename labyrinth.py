#! /usr/bin/env python3
#coding utf-8

import pygame

from wall import *

from constants import *

class Labyrinth(pygame.sprite.Sprite):
    def __init__(self, wall):
        pygame.sprite.Sprite.__init__(self)
        self.wall_image = pygame.image.load(wall)

    def creat_labyrinth(self, structure):
        Y_LOGIC = 0
        with open(structure, "r") as file:
            for line in file:
                print(line)
                X_LOGIC = 0
                for sprite in line:
                    X_GRAPHIC = X_LOGIC*SPRITE_SIZE
                    Y_GRAPHIC = Y_LOGIC*SPRITE_SIZE
                    if sprite == "W":
                        BACKGROUND.blit(self.wall_image, (X_GRAPHIC, Y_GRAPHIC))
                        position_wall = (X_GRAPHIC, Y_GRAPHIC)
                        LIST_OF_OCCUPIED_POSITIONS.append(position_wall)
                    elif sprite == "S":
                        position_start = (X_GRAPHIC, Y_GRAPHIC)
                        LIST_OF_OCCUPIED_POSITIONS.append(position_start)
                    elif sprite == "A":
                        position_arrival = (X_GRAPHIC, Y_GRAPHIC)
                        LIST_OF_OCCUPIED_POSITIONS.append(position_arrival)
                    elif sprite == "0":
                        position_empty = (X_GRAPHIC, Y_GRAPHIC)
                        LIST_EMPTY_POSITIONS.append(position_empty)
                    X_LOGIC += 1
                Y_LOGIC += 1