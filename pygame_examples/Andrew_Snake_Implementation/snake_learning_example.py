import pygame
import time
import random

# Start pygame ;-)
pygame.init()

# Set the window size
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

# Game requires a "title"
pygame.display.set_caption("Snake")

# Get the picture of the snakehead we created
image = pygame.image.load('snake.jpg')

# Explitily define some RGB Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Snek size / apple size
block_size = 20

# Frame rate
FPS = 15
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 25)


# Start the snake head image facing right
direction = 'right'
def snake(block_size, snake_list):
    if direction == 'right':
        head = pygame.transform.rotate(image, 270)
    if direction == 'left':
        head = pygame.transform.rotate(image, 90)  
    if direction == 'up':
        head = image
    if direction == 'down':
        head = pygame.transform.rotate(image, 180)

    # Make the "head" of the snake at each timestep our iamge
    game_display.blit(head, (snake_list[-1][0], snake_list[-1][1]))

    for x_y in snake_list[:-1]:
        pygame.draw.rect(game_display, green, [x_y[0], x_y[1], block_size, block_size])


### TEXT_OBJECTS AND MESSAGE_TO_SCREEN ARE TO GET THE END GAME MESSAGE TO DISPLAY CENTERED
def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, x_displace=0,y_displace=0, size='small'):
    # surface object and the rectangle "shape"
    text_surface, text_rect = text_objects(msg, red)
    
    # get center of the textbox surface
    text_rect.center = (display_width / 2, display_height / 2 + y_displace)
    game_display.blit(text_surface, text_rect)


def game_loop():
    global direction
    
    game_exit = False
    game_over = False


    # Head block of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Spawning the apples
    rand_apple_x = round(random.randrange(0, (display_width - block_size))) #/ 10.0) * 10.0
    rand_apple_y = round(random.randrange(0, (display_height - block_size))) #/ 10.0) * 10.0



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


        # Event is just change in state
        for event in pygame.event.get():
            # if you forget this line you can't exit the game LOL
            if event.type == pygame.QUIT:
                game_exit = True 

            if event.type == pygame.KEYDOWN:
                # L & R
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    # update y velocity so user cant move diagonally
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                # U & D
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    # Update x velocity so user cant move diagonally
                    lead_x_change = 0
                    lead_y_change = -block_size # -y = up
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_x_change = 0
                    lead_y_change = block_size # +y = down
                
            ### Boundaries
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                game_over = True
            
        
        # Change x direction
        lead_x += lead_x_change
        # Change y direction
        lead_y += lead_y_change
        # Background color
        game_display.fill(white)
        # Apple size
        apple_thickness = 30
        # Draw the apple
        pygame.draw.rect(game_display, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # Make sure the rendered snake doesn't exceed snake_len
        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        # Head of the snake
        snake(block_size, snake_list)


        pygame.display.update()

        # Collision Detection for apple and snake
        if lead_x > rand_apple_x and lead_x < (rand_apple_x + apple_thickness) or (lead_x + block_size) > rand_apple_x and (lead_x + block_size) < (rand_apple_x + apple_thickness):
            if lead_y > rand_apple_y and (lead_y < rand_apple_y + apple_thickness) or (lead_y + block_size) > rand_apple_y and (lead_y + block_size) < (rand_apple_y + apple_thickness):
                rand_apple_x = round(random.randrange(0, display_width-block_size))
                rand_apple_y = round(random.randrange(0, display_height-block_size))
                # make the snake 1 block longer
                snake_length += 1


        clock.tick(FPS)



    pygame.quit()
    quit



# Start the game
game_loop()
