
#! /usr/bin/env python3
#coding utf-8

import pygame

SPRITE_SIZE = 32
SPRITE_NUMBER = 15
SPRITE_WIDTH = SPRITE_SIZE*SPRITE_NUMBER
SPRITE_HEIGHT = SPRITE_SIZE*SPRITE_NUMBER

BACKGROUND = pygame.image.load("pictures/meadow.jpg")

GROUP_ITEMS = pygame.sprite.Group()
GROUP_WALLS = pygame.sprite.Group()
GROUP_GLOBAL_SPRITES = pygame.sprite.Group()