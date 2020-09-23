#! /usr/bin/env python3
#coding utf-8

import pygame

from wall import *

from constants import *

class Labyrinth(pygame.sprite.Sprite):
    def __init__(self, path_structure):
        pygame.sprite.Sprite.__init__(self)
        self.structure = path_structure
        self.position = (0,0)
        self.position_wall = (0,0)
        self.list_positions_walls = []
        self.position_empty = []
        self.position_start = ()
        self.position_arrival = ()
        self.seringue = set()

    def creat_labyrinth(self):
        Y_LOGIC = 0
        with open(self.structure, "r") as file:
            for line in file:
                print(line)
                X_LOGIC = 0
                for sprite in line:
                    X_GRAPHIC = X_LOGIC*SPRITE_SIZE
                    Y_GRAPHIC = Y_LOGIC*SPRITE_SIZE
                    self.position = (X_GRAPHIC, Y_GRAPHIC)
                    if sprite == "W":
                        self.position_wall = self.position
                        self.list_positions_walls.append(self.position_wall)
                    elif sprite == "S":
                        self.position_start = self.position
                    elif sprite == "A":
                        self.position_arrival = self.position
                    elif sprite == "0":
                        position_empty = self.position
                        self.position_empty.append(position_empty)
                    X_LOGIC += 1
                Y_LOGIC += 1
    
    def blit_labyrinth(self, path_wall):
        for position_wall in self.list_positions_walls:
            wall = Wall(path_wall)
            wall.placement_wall(position_wall)
            wall.blit_wall(screen)

    def end_game(self, position_hero):
        if position_hero == self.position_arrival:
            if len(self.seringue) == 3:
                print("C'est gagné")
            else:
                print('Cest perdu')