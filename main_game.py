''' This is where the magic happens, here we will initiate the game, run the routines
and call the classes that were defined elsewhere, like Player and Enemy.'''

import pygame
import os
import sys

# Initiates pygame and defines the screen size for the game.
pygame.init()
screen_w, screen_h = 800, 600
screen = pygame.display.set_mode((screen_w,screen_h))


class Character:

    def __init__(self):
        import pygame
        self.health = 100


class Player(Character):

    def __init__(self):
        self.sprite = pygame.image.load("./Personagens/Images/player.png")
# Calls for the Player class
#from Personagens import *
player_01 = Character()