# -*-coding:utf8-*-

import pygame
from game import Game
from pygame_functions import *

"""Fenetre principal de mon programme"""

pygame.init()

# Fenetre de mon jeu

resolution = (640, 480)
pygame.display.set_caption("MonJeu")
screen = pygame.display.set_mode(resolution)

# Charger le jeu 

game = Game()


# Boucle d'initialisation de mon jeu

launched = True

while launched :
    
    # Mettre l'arrière plan

    bg = pygame.image.load("assets/bg.png")
    bg = pygame.transform.scale(bg, resolution)
    rectan = bg.get_rect()
    screen.blit(bg, (0, 0))    # Placer l'arrière plan 
    game.player.render(screen)     # Placer le personnages
    pygame.display.flip()       # Mise à jour de l'écran
    

    if game.pressed.get(pygame.K_RIGHT) :
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) :
        game.player.move_left()

    for event in pygame.event.get() :
        # Tout les évenements qui se dérouleront seront ici
        if event.type == pygame.QUIT :
            launched = False
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False
