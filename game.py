#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *
from wall import *
from labyrinth import *
from hero import *

pygame.init()

#Open the windows of Pygame
screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
#Title
pygame.display.set_caption("SOS MacGyver")

background = pygame.image.load("pictures/meadow.jpg")

#labyrinth = Labyrinth()
#labyrinth.create_labyrinth()
#labyrinth.display_labyrinth(screen)

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