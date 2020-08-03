#! /usr/bin/env python3
#coding utf-8

import pygame
from wall import *
from constants import *

class Labyrinth(pygame.sprite.Sprite):
    """Create labyrinth for game"""
    def __init__(self, file):
        pygame.sprite.Sprite.__init__(self)
        self.file = file
        self.labyrinth = 0
        
    def create_labyrinth():
        with open ("labyrinth.txt", "r") as file:
            new_labyrinth = []
            for line in file:
                new_line = []
                for sprite in line:
                    if sprite != '\n':
                        new_line.append(sprite)
                new_labyrinth.append(new_line)
            self.labyrinth = new_labyrinth
        return self.labyrinth


    def display_labyrinth():
        """Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
	
        wall = pygame.image.load(pictures/wall32.jpg).convert()
		
        num_line = 0
        for line in self.labyrinth:
			#On parcourt les listes de lignes
            num_case = 0
            for sprite in line:
				#On calcule la position réelle en pixels
                x = num_case * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == 'W':
                    screen.blit(wall, (x,y))
                num_case += 1
            num_line += 1
    
