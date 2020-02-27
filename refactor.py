import pygame
import time
import random
import math
from math import hypot
from itertools import combinations

# Start pygame ;-)
pygame.init()

# Set the window size
display_width = 800
display_height = 800
game_display = pygame.display.set_mode((display_width, display_height))

# Set window title
pygame.display.set_caption("Neuralink Surgery Game")

# Game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (155, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)


####################
"""GAME VARIABLES"""
####################
FPS = 15
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 25)


# Image of blood vessel
background_image = pygame.image.load('datasets/training/1st_manual/21_manual1.gif')


def game_loop():
    """The main loop of the neuralink surgery simulator"""
    dead = False

    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True 
        
        # Show the image
        game_display.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(FPS)


# Start the game!
game_loop()