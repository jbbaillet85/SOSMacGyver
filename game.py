#! /usr/bin/env python3
#coding utf-8

import pygame

from labyrinth import *
from guardian import *
from hero import *
from items import *
from wall import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

#create of labyrinth
labyrinth = Labyrinth("labyrinth.txt")
labyrinth.creat_labyrinth("pictures/wall32.jpg")

#creat and placement MacGyver
MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
BACKGROUND.blit(MacGyver.image, (MacGyver.position))

#creat and placement gardian
gardian = Gardian("pictures/Gardien32.png", "Gardian")
BACKGROUND.blit(gardian.image, (gardian.position))

#creat and placement items
aiguille = Items("pictures/seringue32.png", "aiguille")
aiguille.placement_item(labyrinth.position_empty)
labyrinth.position_occuped.append(aiguille.position)
tube = Items("pictures/tube_plastique32.png", "tube")
tube.placement_item(labyrinth.position_empty)
labyrinth.position_occuped.append(tube.position)
ether = Items("pictures/ether32.png", "ether")
ether.placement_item(labyrinth.position_empty)
labyrinth.position_occuped.append(ether.position)

pygame.display.flip()

#Loop of game
end_game = False

while not end_game:

    #loop evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MacGyver.move("L", labyrinth.position_empty)
            elif event.key == pygame.K_RIGHT:
                MacGyver.move("R", labyrinth.position_empty)
            elif event.key ==pygame.K_UP:
                MacGyver.move("U", labyrinth.position_empty)
            elif event.key == pygame.K_DOWN:
                MacGyver.move("D", labyrinth.position_empty)
        
        MacGyver.blit()
        print(MacGyver.position)
        labyrinth.end_game(MacGyver.position)
        screen.blit(BACKGROUND, (0,0))
        pygame.display.flip()