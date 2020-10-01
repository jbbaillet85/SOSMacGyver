# ! /usr/bin/env python3
# coding utf-8

import pygame

from labyrinth import Labyrinth
from guardian import Gardian
from hero import Hero
from items import Items
from constants import screen, black

pygame.init()

pygame.display.set_caption("SOS MacGyver")

# create of labyrinth
labyrinth = Labyrinth("labyrinth.txt")
labyrinth.creat_labyrinth()
labyrinth.blit_labyrinth("pictures/wall32.jpg")

# creat and placement MacGyver
MacGyver = Hero("pictures/MacGyver32.png", "MacGyver")
MacGyver.placement_hero(labyrinth.position_start)
print("position du hero", labyrinth.position_start)
MacGyver.blit(screen)

# creat and placement gardian
gardian = Gardian("pictures/Gardien32.png", "Gardian")
gardian.placement_gardian(labyrinth.position_arrival)
print("position du méchant", gardian.position)
gardian.blit(screen)

# creat and placement items
aiguille = Items("pictures/seringue32.png", "aiguille")
aiguille.placement_item(screen, labyrinth.list_positions_empty)
print("position de l'aiguille", aiguille.position)
tube = Items("pictures/tube_plastique32.png", "tube")
tube.placement_item(screen, labyrinth.list_positions_empty)
print("position du tube", tube.position)
ether = Items("pictures/ether32.png", "ether")
ether.placement_item(screen, labyrinth.list_positions_empty)
print("position de l'ether", ether.position)

pygame.display.flip()

# Loop of game
end_game = False

while not end_game:

    # loop evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MacGyver.move("L", labyrinth.list_positions_empty)
            elif event.key == pygame.K_RIGHT:
                MacGyver.move("R", labyrinth.list_positions_empty)
            elif event.key == pygame.K_UP:
                MacGyver.move("U", labyrinth.list_positions_empty)
            elif event.key == pygame.K_DOWN:
                MacGyver.move("D", labyrinth.list_positions_empty)

        MacGyver.clear_hero(screen, black)
        MacGyver.blit(screen)
        print("MacGyver est en position: ", MacGyver.position)

        aiguille.colision_items(MacGyver.position, labyrinth.seringue)
        tube.colision_items(MacGyver.position, labyrinth.seringue)
        ether.colision_items(MacGyver.position, labyrinth.seringue)
        print("liste des éléments de la seringue", labyrinth.seringue)

        labyrinth.counter_items()

        labyrinth.end_game(MacGyver.position)

        pygame.display.flip()
