''' This is where the magic happens, here we will initiate the game, run the routines
and call the classes that were defined elsewhere, like Player and Enemy.'''

import pygame
import os
import sys
from pygame.locals import *

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
        self.sprite = pygame.image.load("/home/marciomarchiori/Documents/Project_CORONGA/Attack_on_Coronga/Personagens/Images/dude.png")
        self.initial_pos_w = 300
        self.initial_pos_h = 300
# Calls for the Player class
#from Personagens import *
player_01 = Character()


''' This is the core game, the place where it keeps the loop going till it gets
called off'''
while True:
    screen.fill(0)
    screen.blit(player_01,(initial_pos_w, initial_pos_h)
    
    pygame.display.flip() #This line makes the game keep updating
    for event in pygame.event.get(): # Loop everything in place
        if event.type == pygame.QUIT: # If X is pressed it ends de program
            pygame.quit()
            exit(0)

    