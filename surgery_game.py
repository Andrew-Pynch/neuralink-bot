import pygame
import time
import random

# Start pygame ;-)
pygame.init()

# Set the window size
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

# Set window title
pygame.display.set_caption("Neuralink Surgery Game")

# Game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (155, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)


FPS = 15
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 25)


### N0TE: ALL THESE FUNCTIONS ARE JUST A GUESS AT WHAT THE STRUCTURE OF THE PROGRAM WILL BE... ###
def vessels():
    """Create pygame representation of blood vessels"""
    pass


def lace():
    """Represent the neural lace you will be performing surgery with"""
    pass


def score():
    """
    Haven't decided how this is going to be implemented. T
    The score function needs to be really good so that algo becomes
    Excellent at "avoiding" blood vessels...
    """
    pass


def message_to_screen(msg, color, y_displace=0, size='small'):
    # surface object and the rectangle "shape"
    text_surface, text_rect = text_objects(msg, red)
    
    # get center of the textbox surface
    text_rect.center = (display_width / 2, display_height / 2 + y_displace)
    game_display.blit(text_surface, text_rect)


def game_loop():
    game_exit = False
    game_over = False

    while not game_exit:
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game Over!", red)
            message_to_screen("Press C to play again or Q to quit", black, y_displace=50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()


        for event in pygame.event.get():
            # If you forget this line you can't close the game window... LOL
            if event.type == pygame.QUIT:
                game_exit = True 


            ### TO DO: DECIDE IF MOUSE OR KMB SELECTION? Probably kmb for the learner... ###


        ### MAIN GAME ITEMS
        game_display.fill(white)
        pygame.display.update()

        # Render at the framerate ^^^
        clock.tick(FPS)



    pygame.quit()
    quit


