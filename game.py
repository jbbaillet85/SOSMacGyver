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
MacGyver.placement_hero(labyrinth.position_start)
print("position du hero", labyrinth.position_start)
MacGyver.blit()

#creat and placement gardian
gardian = Gardian("pictures/Gardien32.png", "Gardian")
gardian.placement_gardian(labyrinth.position_arrival)
print("position du méchant", gardian.position)
gardian.blit()

#creat and placement items
aiguille = Items("pictures/seringue32.png", "aiguille")
aiguille.placement_item(labyrinth.position_empty)
print("position de l'aiguille", aiguille.position)
labyrinth.position_occuped.append(aiguille.position)
tube = Items("pictures/tube_plastique32.png", "tube")
tube.placement_item(labyrinth.position_empty)
print("position du tube", tube.position)
labyrinth.position_occuped.append(tube.position)
ether = Items("pictures/ether32.png", "ether")
ether.placement_item(labyrinth.position_empty)
print("position de l'ether", ether.position)
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

        aiguille.colision_items(MacGyver.position, labyrinth.set_items)
        tube.colision_items(MacGyver.position, labyrinth.set_items)
        ether.colision_items(MacGyver.position, labyrinth.set_items)
        print("liste des items", labyrinth.set_items)

        labyrinth.end_game(MacGyver.position)

        screen.blit(BACKGROUND, (0,0))
        pygame.display.flip()