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


def snake(block_size, snake_list):
    for x_y in snake_list:
        pygame.draw.rect(game_display, green, [x_y[0], x_y[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width / 2, display_height / 2])


def game_loop():
    game_exit = False
    game_over = False


    # Head block of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Spawning the apples
    rand_apple_x = round(random.randrange(0, (display_width - block_size))) #/ 10.0) * 10.0
    rand_apple_y = round(random.randrange(0, (display_height - block_size))) #/ 10.0) * 10.0



    while not game_exit:

        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game Over! Press C to play again or Q to quit", red)
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
                    lead_x_change = -block_size
                    # update y velocity so user cant move diagonally
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                # U & D
                elif event.key == pygame.K_UP:
                    # Update x velocity so user cant move diagonally
                    lead_x_change = 0
                    lead_y_change = -block_size # -y = up
                elif event.key == pygame.K_DOWN:
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
