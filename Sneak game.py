
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define the snake and food
snake_size = 10
snake_x = window_width // 2
snake_y = window_height // 2
snake_speed = 15
snake_body = [(snake_x, snake_y)]
snake_direction = (1, 0)  # initial direction is right

food_x = random.randrange(0, window_width - snake_size, snake_size)
food_y = random.randrange(0, window_height - snake_size, snake_size)

# Define the game clock
clock = pygame.time.Clock()

# Define the game font
font = pygame.font.Font(None, 36)

# Game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction!= (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction!= (-1, 0):
                snake_direction = (1, 0)
            elif event.key == pygame.K_UP and snake_direction!= (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction!= (0, -1):
                snake_direction = (0, 1)

    # Move the snake
    snake_x += snake_direction[0] * snake_size
    snake_y += snake_direction[1] * snake_size

    # Update the snake's body
    snake_body.insert(0, (snake_x, snake_y))
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, window_width - snake_size, snake_size)
        food_y = random.randrange(0, window_height - snake_size, snake_size)
    else:
        snake_body.pop()

    # Check for collisions
    if (snake_x < 0 or snake_x >= window_width or
            snake_y < 0 or snake_y >= window_height or
            (snake_x, snake_y) in snake_body[1:]):
        game_over = True

    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, RED, (food_x, food_y, snake_size, snake_size))

    # Draw the score
    score = len(snake_body) - 1
    score_text = font.render(f"Score: {score}", True, YELLOW)
    window.blit(score_text, (10, 10))

    # Draw the game border
    pygame.draw.rect(window, BLUE, (0, 0, window_width, window_height), 5)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()