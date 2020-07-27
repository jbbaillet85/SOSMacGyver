
#! /usr/bin/env python3
#coding utf-8

import pygame

SPRITE_TAILLE = 30
SPRITE_NUMBER = 15
SPRITE_WIDTH = SPRITE_TAILLE*SPRITE_NUMBER
SPRITE_HEIGHT = SPRITE_TAILLE*SPRITE_NUMBER

GROUP_OBJECTS = pygame.sprite.Group()
GROUP_WALLS = pygame.sprite.Group()
GROUP_GLOBAL_SPRITES = pygame.sprite.Group()