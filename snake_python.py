import pygame
import pygame.mixer
import random
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

width = 795
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


font = pygame.font.SysFont(None, 48)

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 204, 102)

snake_block = 15
snake_speed = 15

snake_x = width // 2 - (width // 2) % snake_block
snake_y = height // 2 - (height // 2) % snake_block

snake_dx = 0
snake_dy = 0


# Adjust the initial food position to align with the grid
food_x = (round(random.randrange(0, width - snake_block) / snake_block)) * snake_block
food_y = (round(random.randrange(0, height - snake_block) / snake_block)) * snake_block

snake_length = 1
snake_segments = []

clock = pygame.time.Clock()
start_time = time.time()
current_time = 0
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_block
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_block
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -snake_block
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = snake_block
                snake_dx = 0

    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x == food_x and snake_y == food_y:
        snake_length += 1

        # Adjust the position of the food item to align with the grid
        food_x = (round(random.randrange(0, width - snake_block) / snake_block)) * snake_block
        food_y = (round(random.randrange(0, height - snake_block) / snake_block)) * snake_block

    snake_head = [snake_x - (snake_x % snake_block), snake_y - (snake_y % snake_block)]
    snake_segments.append(snake_head)


    if len(snake_segments) > snake_length:
        del snake_segments[0]

    for segment in snake_segments[:-1]:
        if segment == snake_head:
            running = False

    win.fill(black)

    if snake_x > width or snake_x < 0 or snake_y > height or snake_y < 0:
        running = False
    
    grid_size = 15
    for x in range(0, width, grid_size):
        pygame.draw.line(win, (64, 64, 64), (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(win, (64, 64, 64), (0, y), (width, y))

    current_time = int(time.time() - start_time)
    timer_text = font.render(str(current_time), True, white)
    win.blit(timer_text, (10,10))

    score_num = int(snake_length)
    score_text = font.render("Score: " + str(score_num), True, white)
    win.blit(score_text, (398,10))

    for segment in snake_segments:
        pygame.draw.rect(win, white, (segment[0], segment[1], snake_block, snake_block))

    pygame.draw.rect(win, green, (food_x, food_y, snake_block, snake_block))

    pygame.display.update()


    clock.tick(snake_speed)

pygame.mixer.music.stop()

pygame.quit()
