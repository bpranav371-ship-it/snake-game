import pygame
import random

# Initialize pygame
pygame.init()
int a=12

# Screen size
width = 800
height = 800
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Kore Head")

# Clock
clock = pygame.time.Clock()

# Snake settings
snake_block = 20
snake_speed = 9

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Load snake head image
snake_head_img = pygame.image.load("IMG-20241110-WA0009.png")
snake_head_img = pygame.transform.smoothscale(snake_head_img, (snake_block, snake_block))

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 30)

# Display score
def score_display(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Draw snake with head image
def draw_snake(snake_block, snake_list):
    for i, pos in enumerate(snake_list):
        if i == len(snake_list) - 1:  # head
            dis.blit(snake_head_img, (pos[0], pos[1]))
        else:
            pygame.draw.rect(dis, green, [pos[0], pos[1], snake_block, snake_block])

# Show message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Game loop
def game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_block) / 20) * 20
    food_y = round(random.randrange(0, height - snake_block) / 20) * 20

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Game Over! Press C-Play Again or Q-Quit", red)
            score_display(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change

        dis.fill(black)
        pygame.draw.rect(dis, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(snake_length - 1)
        pygame.display.update()

        # If snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20) * 20
            food_y = round(random.randrange(0, height - snake_block) / 20) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()
