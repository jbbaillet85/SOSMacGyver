#! /usr/bin/env python3
#coding utf-8

import pygame

from wall import *

from constants import *

class Labyrinth(pygame.sprite.Sprite):
    def __init__(self, path_structure):
        pygame.sprite.Sprite.__init__(self)
        self.structure = path_structure
        self.position_empty = []
        self.position_occuped = []
        self.position_start = ()
        self.position_arrival = ()
        self.set_items = set()

    def creat_labyrinth(self, path_wall):
        wall = Wall(path_wall)
        Y_LOGIC = 0
        with open(self.structure, "r") as file:
            for line in file:
                print(line)
                X_LOGIC = 0
                for sprite in line:
                    X_GRAPHIC = X_LOGIC*SPRITE_SIZE
                    Y_GRAPHIC = Y_LOGIC*SPRITE_SIZE
                    if sprite == "W":
                        BACKGROUND.blit(wall.image, (X_GRAPHIC, Y_GRAPHIC))
                        position_wall = (X_GRAPHIC, Y_GRAPHIC)
                        self.position_occuped.append(position_wall)
                    elif sprite == "S":
                        self.position_start = (X_GRAPHIC, Y_GRAPHIC)
                        self.position_occuped.append(self.position_start)
                    elif sprite == "A":
                        self.position_arrival = (X_GRAPHIC, Y_GRAPHIC)
                        self.position_occuped.append(self.position_arrival)
                    elif sprite == "0":
                        position_empty = (X_GRAPHIC, Y_GRAPHIC)
                        self.position_empty.append(position_empty)
                    X_LOGIC += 1
                Y_LOGIC += 1
        
    def end_game(self, position_hero):
        if position_hero == self.position_arrival:
            if len(self.set_items) == 3:
                print("C'est gagné")
                pygame.quit()
            else:
                print('Cest perdu')
                pygame.quit()