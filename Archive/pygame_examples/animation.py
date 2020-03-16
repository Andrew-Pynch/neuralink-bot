import pygame
import sys 
from pygame.locals import *

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

FPS = 30

xpos = 250
ypos = 250

pygame.init()
DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption('Animate')

while True:
    DISPLAY.fill(WHITE)
    # Draw Rectangle
    box = 10
    pygame.draw.rect(DISPLAY, RED, (xpos, ypos, box, box))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()