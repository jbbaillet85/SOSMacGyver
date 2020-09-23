
#! /usr/bin/env python3
#coding utf-8

import pygame

SPRITE_SIZE = 32
SPRITE_NUMBER = 15
SPRITE_WIDTH = SPRITE_SIZE*SPRITE_NUMBER
SPRITE_HEIGHT = SPRITE_SIZE*SPRITE_NUMBER

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
black = pygame.image.load("pictures/black.jpeg").convert_alpha()