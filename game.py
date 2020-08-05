#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *
from hero import *
from guardian import *
from items import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

background = pygame.image.load("pictures/meadow.jpg")

MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
Gardian = Gardian("pictures/Gardien32.png", "Gardian")
aiguille = Items("pictures/seringue32.png", "aiguille")
tube = Items("pictures/tube_plastique32.png", "tube")
ether = Items("pictures/ether32.png", "ether")
wall = pygame.image.load("pictures/wall32.jpg").convert_alpha()

num_line = 0
with open("labyrinth.txt", "r") as file:
    for line in file:
        num_box = 0
        for sprite in line:
            x = num_box*SPRITE_SIZE
            y = num_line*SPRITE_SIZE
            if sprite == "W":
                background.blit(wall,(x, y))
            elif sprite == "S":
                background.blit(MacGyver.image,(x,y))
            elif sprite == "A":
                background.blit(Gardian.image,(x,y))
            num_box += 1
        num_line += 1

pygame.display.flip()

#Loop of game
while True:

    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    #Affichages aux nouvelles positions
    screen.blit(background, (0,0))
    
    GROUP_GLOBAL_SPRITES.update()
    GROUP_GLOBAL_SPRITES.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()