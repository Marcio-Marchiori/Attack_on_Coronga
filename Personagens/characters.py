'''Initiate class characters with base attributes such as health and other stats that 
may be used by the characters, after attributing the base common attributes it goes
and defines classes for the Player and for the Enemy '''

class Character:

    def __init__(self):
        
        import pygame

        self.health = 100


class Player(Character):

    def __init__(self):
        self.sprite = pygame.image.load("./Personagens/Images/player.png")


class Enemy(Character):
