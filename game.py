#! /usr/bin/env python3
#coding utf-8

import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("SOS MacGyver")

pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break