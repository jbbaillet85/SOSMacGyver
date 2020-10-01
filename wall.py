# ! /usr/bin/env python3
# coding utf-8

import pygame
from constants import screen


class Wall(pygame.sprite.Sprite):
    """Create walls for labyrinth"""
    def __init__(self, img_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.position = (self.rect.x, self.rect.y)

    def placement_wall(self, position_wall):
        self.position = position_wall

    def blit_wall(self, screen):
        screen.blit(self.image, self.position)

    def list_walls(self, list_walls):
        list_walls.append(self.position)
