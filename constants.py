# ! /usr/bin/env python3
# coding utf-8

import pygame

SPRITE_SIZE = 32
SPRITE_NUMBER = 16
SPRITE_WIDTH = SPRITE_SIZE*SPRITE_NUMBER
SPRITE_HEIGHT = SPRITE_SIZE*(SPRITE_NUMBER-1)

screen = pygame.display.set_mode((SPRITE_HEIGHT, SPRITE_WIDTH))
black = pygame.image.load("pictures/black.jpeg").convert_alpha()

win = pygame.image.load("pictures/win.jpg").convert_alpha()
lost = pygame.image.load("pictures/lost.jpg").convert_alpha()
