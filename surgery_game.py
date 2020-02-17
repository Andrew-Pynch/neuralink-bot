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



def lace(x, y, lace_index, lace_size, laces):
    """
    Represent the neural lace you will be performing surgery with
    
    PARAMETERS:
        lace_size: size of the lace on screen
        lace_coordinates: the x, y posistion of the lace on screen
    """
    # list of tuples of laces 
    for each_lace in laces:
        pygame.draw.rect(game_display, blue, [each_lace[0], each_lace[1], lace_size, lace_size])




def score():
    """
    Haven't decided how this is going to be implemented. T
    The score function needs to be really good so that algo becomes
    Excellent at "avoiding" blood vessels...
    """
    pass


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


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

    # All of the threads on screen
    laces = []

    # X AND Y COORDS OF THE LACE
    x = display_width / 2
    y = display_height / 2
    # Change in direction of lace at each timestep
    x_change = 0
    y_change = 0

    lace_counter = 10
    lace_index = 0
    

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
                    x_change = -lace_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = lace_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -lace_size # negative y = up in pygame
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = lace_size # positive y = down
                    x_change = 0
                elif event.key == pygame.K_BACKSPACE:
                    print("Backspace key pressed")
                    lace_counter -= 1
                    lace_index += 1
                    laces.append([x, y])
                    

            """### STOP MOVING WHEN KEY IS RELEASED ###"""
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = 0 # negative y = up in pygame
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 0 # positive y = down
                    x_change = 0
                

            
            """GAME BOUNDARIES"""
            if x >= display_width or x < 0 or y >= display_height or y < 0:
                game_over = True
            

        """UPDATE POSISTION OF LACE BASED OFF PLAYER INPUT"""
        # Set posistion based on velocity
        x += x_change
        y += y_change
        current_lace = [x, y]

        # We have to render the background first since layers are in order from furthest to closest
        game_display.fill(white)
        """### FUNCTIONALIZE THIS ###"""
        


        """MAIN GAME ITEMS"""

        pygame.display.update()

        """Render at the framerate ^^^"""
        clock.tick(FPS)



    pygame.quit()
    quit



# Start the game!
game_loop()
