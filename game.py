#! /usr/bin/env python3
#coding utf-8

import random

import pygame

from constants import *
from wall import *
from hero import *
from guardian import *
from items import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")
background = pygame.image.load("pictures/meadow.jpg")

#sprites of game:
MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
Gardian = Gardian("pictures/Gardien32.png", "Gardian")
GROUP_GLOBAL_SPRITES.add(MacGyver, Gardian)

wall = Wall("pictures/wall32.jpg")

aiguille = Items("pictures/seringue32.png", "aiguille")
tube = Items("pictures/tube_plastique32.png", "tube")
ether = Items("pictures/ether32.png", "ether")
GROUP_ITEMS.add(aiguille, tube, ether)

#create of labyrinth
Y_LOGIC = 0
with open("labyrinth.txt", "r") as file:
    for line in file:
        print(line)
        X_LOGIC = 0
        for sprite in line:
            X_GRAPHIC = X_LOGIC*SPRITE_SIZE
            Y_GRAPHIC = Y_LOGIC*SPRITE_SIZE
            if sprite == "W":
                background.blit(wall.image,(X_GRAPHIC, Y_GRAPHIC))
                position_wall = (X_GRAPHIC, Y_GRAPHIC)
                LIST_OF_OCCUPIED_POSITIONS.append(position_wall)
                GROUP_WALLS.add(wall)
                GROUP_GLOBAL_SPRITES.add(wall)
            elif sprite == "S":
                background.blit(MacGyver.image,(X_GRAPHIC,Y_GRAPHIC))
                position_start = (X_GRAPHIC, Y_GRAPHIC)
                LIST_OF_OCCUPIED_POSITIONS.append(position_start)
            elif sprite == "A":
                background.blit(Gardian.image,(X_GRAPHIC,Y_GRAPHIC))
                position_arrival = (X_GRAPHIC, Y_GRAPHIC)
                LIST_OF_OCCUPIED_POSITIONS.append(position_arrival)
            elif sprite == "0":
                position_empty = (X_GRAPHIC, Y_GRAPHIC)
                LIST_EMPTY_POSITIONS.append(position_empty)
            X_LOGIC += 1
        Y_LOGIC += 1

#placement items 
background.blit(aiguille.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_OF_OCCUPIED_POSITIONS.append(aiguille.position)
background.blit(tube.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_OF_OCCUPIED_POSITIONS.append(tube.position)
background.blit(ether.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_OF_OCCUPIED_POSITIONS.append(ether.position)

GROUP_GLOBAL_SPRITES.add(aiguille, tube, ether)
pygame.display.flip()

#Loop of game
end_game = False

while not end_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MacGyver.move("L")
            elif event.key == pygame.K_RIGHT:
                MacGyver.move("R")
            elif event.key ==pygame.K_UP:
                MacGyver.move("U")
            elif event.key == pygame.K_DOWN:
                MacGyver.move("D")
    
        screen.blit(background, (0,0))
        background.blit(MacGyver.image, (MacGyver.position))
        GROUP_GLOBAL_SPRITES.update()
        pygame.display.flip()