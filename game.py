#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *
from labyrinth import *
from hero import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

background = pygame.image.load("pictures/meadow.jpg")

MacGyver = pygame.image.load("pictures/MacGyver32.png").convert_alpha()
Gardian = pygame.image.load("pictures/Gardien32.png").convert_alpha()
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
                background.blit(MacGyver,(x,y))
            elif sprite == "A":
                background.blit(Gardian,(x,y))
            num_box += 1
        num_line += 1

pygame.display.flip()

#Loop of game
while True:

    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    #Affichages aux nouvelles positions
    screen.blit(background, (0,0))
    
    #labyrinth.display_labyrinth(screen)
    GROUP_GLOBAL_SPRITES.update()
    GROUP_GLOBAL_SPRITES.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()