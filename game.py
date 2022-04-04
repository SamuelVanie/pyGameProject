import pygame
from player import Player

# CLasse qui represente mon jeu 

class Game :
    
    def __init__(self) :
        
        # Generer le joueur
        self.player = Player() 
        self.pressed = {}
        
