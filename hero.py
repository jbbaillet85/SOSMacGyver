#! /usr/bin/env python3
#coding utf-8

import pygame

from constants import *


class Hero(pygame.sprite.Sprite):
    """Create hero for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.position = (self.rect.x, self.rect.y)
        self.list_positions_hero = [self.position, self.position]
        self.position_previous = self.list_positions_hero[-2]
    
    def move(self, direction, list_position_wall, position_start):
        """methode move for Hero"""
        if direction == "L":
            if self.rect.x > 0:
                self.rect.x -= SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
                self.colision_walls(list_position_wall)
        elif direction == "R":
            if self.rect.x < SPRITE_SIZE*(SPRITE_NUMBER-1):
                self.rect.x += SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
                self.colision_walls(list_position_wall)
        elif direction == "U":
            if self.rect.y > 0:
                self.rect.y -= SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
                self.colision_walls(list_position_wall)
        elif direction == "D":
            if self.rect.y < SPRITE_SIZE*(SPRITE_NUMBER-1):
                self.rect.y += SPRITE_SIZE
                self.position = (self.rect.x, self.rect.y)
                self.colision_walls(list_position_wall)
        return self.position
    

    def placement_hero (self, position_start):
        self.position = position_start

    def blit(self, screen):
        screen.blit(self.image,(self.position))
    
    def creat_list_positions_hero(self):
        self.list_positions_hero.append(self.position)
    
    def clear_hero(self, screen, black):
        self.creat_list_positions_hero()
        self.position_previous = self.list_positions_hero[-2]
        screen.blit(black, self.position_previous)
    
    def colision_walls(self, list_position_wall):
        if self.position in list_position_wall:
            self.position = self.list_positions_hero[-1]
        return self.position