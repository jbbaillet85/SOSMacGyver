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
        #On ouvre le fichier
        with open ("labyrinth.txt", "r") as file:
            new_labyrinth = []
            #On parcourt les lignes du fichier
            for line in file:
                new_line = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in line:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
    					#On ajoute le sprite à la liste de la ligne
                        new_line.append(sprite)
                        #On ajoute la ligne à la liste du niveau
                new_labyrinth.append(new_line)
			#On sauvegarde cette structure
            self.labyrinth = new_labyrinth
        return self.labyrinth


    def display_labyrinth():
        """Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
        wall = pygame.image.load(pictures/wall32.jpg).convert()
		
		#On parcourt la liste du niveau
        num_line = 0
        for line in self.labyrinth:
			#On parcourt les listes de lignes
            num_case = 0
            for sprite in line:
				#On calcule la position réelle en pixels
                x = num_case * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == 'M':		   #m = Mur
                    screen.blit(wall, (x,y))
                num_case += 1
            num_line += 1
    
