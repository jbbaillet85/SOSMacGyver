# ! /usr/bin/env python3
# coding utf-8

import pygame


class Gardian (pygame.sprite.Sprite):
    """Create gardian for labyrinth"""
    def __init__(self, img_path, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.position = (self.rect.x, self.rect.y)

    def placement_gardian(self, position_arrival):
        self.position = position_arrival

    def blit(self, screen):
        screen.blit(self.image, (self.position))
