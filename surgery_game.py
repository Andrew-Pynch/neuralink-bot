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

# Size of the neural lace on screen
lace_size = 10
lace_max = 9
# List of laces
lace_list = []

# Size of the vessel on the screen
vessel_size = 10
# List of fractal coordinates:
vessel_list = []


### N0TE: ALL THESE FUNCTIONS ARE JUST A GUESS AT WHAT THE STRUCTURE OF THE PROGRAM WILL BE... ###
def vessel_fractal(x1, y1, angle, depth, vessel_list):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)

        # Render the paramters that were passed in
        pygame.draw.line(game_display, red, (x1, y1), (x2, y2), 2)

        # Render the left branch and add its coordinates to the list
        vessel_fractal(x2, y2, angle - 20, depth - 1, vessel_list)
        vessel_list.append([x2, y2])
        # Render the right branch and add its coordinates to the list
        vessel_fractal(x2, y2, angle + 20, depth - 1, vessel_list)
        vessel_list.append([x2, y2])

    return vessel_list


def render_vessels(vessel_length, vessel_list, pulse=0, degree=90):
    """RENDER ALL THE VESSELS"""

    ### CENTRAL VEINS ###
    vessel_fractal(display_width/2+pulse, display_height/2+pulse, -degree, vessel_length, vessel_list)
    vessel_fractal(display_width/2+pulse, display_height/2+pulse, 90-degree, vessel_length, vessel_list)
    vessel_fractal(display_width/2+pulse, display_height/2+pulse, degree, vessel_length, vessel_list)
    vessel_fractal(display_width/2+pulse, display_height/2+pulse, degree+90, vessel_length, vessel_list)

    ### OUTER VEINS POINTING INWARDS ###
    vessel_fractal(0+pulse, 0+pulse, degree-45, vessel_length, vessel_list)
    vessel_fractal(display_width+pulse, 0+pulse, degree-315, vessel_length, vessel_list)
    vessel_fractal(0+pulse, display_height+pulse, degree-135, vessel_length, vessel_list)
    vessel_fractal(display_width+pulse, display_height+pulse, degree+135, vessel_length, vessel_list)


def render_lace(x, y, lace_list):
    """SHOW LACE COUNTER IN TOP LEFT"""
    remaining_laces = str(10 - len(lace_list))
    lace_message = ("%s laces remain" % remaining_laces)
    message_to_screen(lace_message, black, -display_width/2.5, -display_height/2.25)

    """### RENDER ALL THE LACES ###"""
    # RENDER THE CURRENT LACE
    pygame.draw.rect(game_display, blue, [x, y, lace_size, lace_size])
    for point in lace_list:
        if lace_list.count(point) > 1:
            message_to_screen("Sorry, you can't place a lace in the same spot", red, display_width/4, -display_height/2.25)
        else:
            pygame.draw.rect(game_display, green, [point[0], point[1], lace_size, lace_size])


def lace_cleanup(lace_list): 
    """The magical but jenky function that prevents duplicate laces from being placed"""
    for point in lace_list: 
        if lace_list.count(point) > 1: lace_list.remove(point)


def score(lace_list, vessel_list):
    """Score = Σ(Euclidean Distance(for point in points_list))"""
    ### TODO: Fix error checking on reducing score when a lace collides with a blood vessel
    score = 0

    """Turn points in lace_list and vessel_list into tuples for faster processing"""
    for point in lace_list:
        point = tuple(point)
    # for point in vessel_list:
    #     point = tuple(point)

    # Compute the distance between each point and every other point in the list
    lace_distance_list = [compute_euclidean(*combo) for combo in combinations(lace_list,2)]

    score = int(sum(lace_distance_list))

    """REDUCE SCORE FOR COLLIDING WITH A BLOOD VESSEL"""
    #https://djangostars.com/blog/list-comprehensions-and-generator-expressions/

    message = ("Score: %s" % score)
    message_to_screen(message, black, -display_width/2.5, +display_height/2.5)

def score_cumulative(lace_list, vessel_list, score):
    """Score = Σ(Euclidean Distance(for point in points_list))"""
    ### TODO: Fix error checking on reducing score when a lace collides with a blood vessel
    # REMOVE SCORE = 0 such that score variable isn't reset every time
    # score = 0

    """Turn points in lace_list and vessel_list into tuples for faster processing"""
    for point in lace_list:
        point = tuple(point)
    # for point in vessel_list:
    #     point = tuple(point)

    # Compute the distance between each point and every other point in the list
    lace_distance_list = [compute_euclidean(*combo) for combo in combinations(lace_list,2)]

    score += int(sum(lace_distance_list))

    """REDUCE SCORE FOR COLLIDING WITH A BLOOD VESSEL"""
    #https://djangostars.com/blog/list-comprehensions-and-generator-expressions/

    message = ("Score: %s" % score)
    message_to_screen(message, black, -display_width/2.5, +display_height/2.5)

def compute_euclidean(p1, p2):
    """Euclidean distance between two points."""
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    return hypot(x2 - x1, y2 - y1)
    

def lose_condition(lace_list):
    if len(lace_list) >= 10:    #if more than 9 laces,
        return True             #player loses


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, x_displace=0, y_displace=0, size='small'):
    """Display a message on the screen!"""
    # surface object and the rectangle "shape"
    text_surface, text_rect = text_objects(msg, color)
    
    # get center of the textbox surface
    text_rect.center = (display_width / 2 + x_displace, display_height / 2 + y_displace)
    game_display.blit(text_surface, text_rect)


def game_loop():
    """The main loop of the neuralink surgery simulator"""
    game_exit = False
    game_over = False
    score = 0

    # Current lace we are rendering
    current_lace = 0

    """RENDER THE VESSELS ON SCREEN"""


    # X AND Y COORDS OF THE LACE
    x = display_width / 2
    y = display_height / 2
    # Change in direction of lace at each timestep
    x_change = 0
    y_change = 0
    

    while not game_exit:
        # Basically just check if we have placed all the laces
        if lose_condition(lace_list) == True:
            game_over = True
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game Over!", red)
            message_to_screen("Final score:", red)      #print the final score to the screen
            message_to_screen("Press C to play again or Q to quit", black, y_displace=50)
            # Reset lace_list (otherwise it will render laces placed during the last run)
            del lace_list[:]
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
                    y_change = +lace_size # negative y = up in pygame
                    x_change = 0
                elif event.key == pygame.K_BACKSPACE:
                    """### ADD THIS TO LACE FUNCTION ###"""
                    # Get current coordinates
                    x += x_change
                    y += y_change
                    # Place in list
                    placed_lace = [x, y]
                    # Add to lace_list
                    lace_list.append(placed_lace)
                    # Increment current_lace
                    current_lace += 1
                    # PRINT LINE FOR TESTING
                    print(lace_list)


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

        # We have to render the background first since layers are in order from furthest to closest
        game_display.fill(white)

        """RENDER ALL THE VESSELS"""
        vessel_length = 8
        pulse = 15
        for i in range(FPS // 2):
            random_scalar = random.randint(-10, 10)
            render_vessels(vessel_length, vessel_list, random_scalar)

        """### RENDER ALL THE LACES ###"""
        render_lace(x, y, lace_list)
        score(lace_list, vessel_list)
        # score_cumulative(lace_list, vessel_list, score)       # enable for "hard mode"

        # Cleanup lace list
        lace_cleanup(lace_list)

        """MAIN GAME ITEMS"""
        pygame.display.update()

        """Render at the framerate ^^^"""
        clock.tick(FPS)


    pygame.quit()
    quit


# Start the game!
game_loop()
