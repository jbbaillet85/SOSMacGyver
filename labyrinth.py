#! /usr/bin/env python3
#coding utf-8

import pygame
from wall import *
from constants import *

class Labyrinth(pygame.sprite.Sprite):
    """Create labyrinth for game"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)