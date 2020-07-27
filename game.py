#! /usr/bin/env python3
#coding utf-8

import pygame
from constants import *
from wall import *

pygame.init()

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
pygame.display.set_caption("SOS MacGyver")

create_labyrinth()

pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break