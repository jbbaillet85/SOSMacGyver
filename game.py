#! /usr/bin/env python3
#coding utf-8

import pygame
import random
from constants import *
from wall import *
from hero import *
from guardian import *
from items import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

background = pygame.image.load("pictures/meadow.jpg")

MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
Gardian = Gardian("pictures/Gardien32.png", "Gardian")

wall = Wall("pictures/wall32.jpg")

aiguille = Items("pictures/seringue32.png", "aiguille")
tube = Items("pictures/tube_plastique32.png", "tube")
ether = Items("pictures/ether32.png", "ether")

num_line = 0
with open("labyrinth.txt", "r") as file:
    for line in file:
        num_box = 0
        for sprite in line:
            x = num_box*SPRITE_SIZE
            y = num_line*SPRITE_SIZE
            if sprite == "W":
                background.blit(wall.image,(x, y))
                GROUP_WALLS.add(wall)
                GROUP_GLOBAL_SPRITES.add(wall)
            elif sprite == "S":
                background.blit(MacGyver.image,(x,y))
                GROUP_GLOBAL_SPRITES.add(MacGyver)
            elif sprite == "A":
                background.blit(Gardian.image,(x,y))
                GROUP_GLOBAL_SPRITES.add(Gardian)
            elif sprite == "0":
                background.blit(aiguille.image, (aiguille.rect.x, aiguille.rect.y))
                background.blit(tube.image, (tube.rect.x, tube.rect.y))
                background.blit(ether.image, (ether.rect.x, ether.rect.y))
                GROUP_ITEMS.add(aiguille, tube, ether)
                GROUP_GLOBAL_SPRITES.add(aiguille, tube, ether)
            num_box += 1
        num_line += 1

pygame.display.flip()

#Loop of game
while True:

    pygame.time.Clock().tick(30)
    
    GROUP_GLOBAL_SPRITES.update()
    GROUP_GLOBAL_SPRITES.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
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
    pygame.display.flip()