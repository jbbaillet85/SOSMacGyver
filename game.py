#! /usr/bin/env python3
#coding utf-8

import pygame

<<<<<<< HEAD
=======
from labyrinth import *
>>>>>>> 0e86eee4f069cd4d465ce9336dbf21e90e9f305c
from guardian import *
from hero import *
from items import *
from wall import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

#create of labyrinth
labyrinth = Labyrinth("pictures/wall32.jpg")
labyrinth.creat_labyrinth("labyrinth.txt")

#creat and placement MacGyver
MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
BACKGROUND.blit(MacGyver.image, (MacGyver.position))

#creat and placement gardian
gardian = Gardian("pictures/Gardien32.png", "Gardian")
BACKGROUND.blit(gardian.image, (gardian.position))

#creat and placement items
aiguille = Items("pictures/seringue32.png", "aiguille")
BACKGROUND.blit(aiguille.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_ITEMS.append(aiguille.position)
tube = Items("pictures/tube_plastique32.png", "tube")
BACKGROUND.blit(tube.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_ITEMS.append(tube.position)
ether = Items("pictures/ether32.png", "ether")
BACKGROUND.blit(ether.image, random.choice(LIST_EMPTY_POSITIONS))
LIST_ITEMS.append(ether.position)

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
                MacGyver.move("L")
            elif event.key == pygame.K_RIGHT:
                MacGyver.move("R")
            elif event.key ==pygame.K_UP:
                MacGyver.move("U")
            elif event.key == pygame.K_DOWN:
                MacGyver.move("D")
        
        MacGyver.exit(gardian.position)
        screen.blit(BACKGROUND, (0,0))
        pygame.display.flip()