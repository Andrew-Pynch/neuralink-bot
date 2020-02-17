import pygame
import time
import random

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

# Size of the neural lace on screen
lace_size = 10
lace_coordinates = [0, 0]


### N0TE: ALL THESE FUNCTIONS ARE JUST A GUESS AT WHAT THE STRUCTURE OF THE PROGRAM WILL BE... ###
def vessels():
    """Create pygame representation of blood vessels"""



def lace(x, y, lace_size):
    """
    Represent the neural lace you will be performing surgery with
    
    PARAMETERS:
        lace_size: size of the lace on screen
        lace_coordinates: the x, y posistion of the lace on screen
    """
    # Render the lace on screen




def score():
    """
    Haven't decided how this is going to be implemented. T
    The score function needs to be really good so that algo becomes
    Excellent at "avoiding" blood vessels...
    """
    pass


def message_to_screen(msg, color, y_displace=0, size='small'):
    """Display a message on the screen!"""
    # surface object and the rectangle "shape"
    text_surface, text_rect = text_objects(msg, red)
    
    # get center of the textbox surface
    text_rect.center = (display_width / 2, display_height / 2 + y_displace)
    game_display.blit(text_surface, text_rect)


def game_loop():
    """The main loop of the neuralink surgery simulator"""
    game_exit = False
    game_over = False


    # X AND Y COORDS OF THE LACE
    x = display_width / 2
    y = display_height / 2
    # Change in direction of lace at each timestep
    x_change = 0
    y_change = 0
    

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


        """Main Game Section"""
        for event in pygame.event.get():
            # If you forget this line you can't close the game window... LOL
            if event.type == pygame.QUIT:
                game_exit = True 
            
            """### MOVEMENT ###"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10 # negative y = up in pygame
                elif event.key == pygame.K_DOWN:
                    y_change = 10 # positive y = down

            
            """GAME BOUNDARIES"""
            if x >= display_width or x < 0 or y >= display_height or y < 0:
                game_over = True
            

        """UPDATE POSISTION OF LACE BASED OFF PLAYER INPUT"""
        # We have to render the background first since layers are in order from furthest to closest
        game_display.fill(white)
        # Set posistion to velocity
        x += x_change
        x_change = 0 # Reset velocity to 0 after each move

        y += y_change
        y_change = 0 # Reset velocity to 0 after each move
        pygame.draw.rect(game_display, blue, [x, y, lace_size, lace_size])


        """MAIN GAME ITEMS"""

        pygame.display.update()

        """Render at the framerate ^^^"""
        clock.tick(FPS)



    pygame.quit()
    quit



# Start the game!
game_loop()
