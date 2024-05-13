# ALL CODE IS CHATGPTED. NOT MINE.

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
GRAVITY = 0.25
BIRD_MOVEMENT = 0

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Load images
bird_surface = pygame.image.load('bird.png').convert_alpha()  # Add your bird image path
bird_rect = bird_surface.get_rect(center=(100, SCREEN_HEIGHT // 2))

background_surface = pygame.image.load('background.jpg').convert()  # Add your background image path

# Pipe
pipe_surface = pygame.image.load('pipe.png').convert()  # Add your pipe image path
pipe_list = []
PIPE_SPAWN = pygame.USEREVENT
pygame.time.set_timer(PIPE_SPAWN, 1200)
pipe_height = [200, 300, 400]

def create_pipe():
    random_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_height))
    top_pipe = pipe_surface.get_rect(midbottom=(500, random_height - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 600:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -BIRD_MOVEMENT * 3, 1)
    return new_bird

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BIRD_MOVEMENT = 0
                BIRD_MOVEMENT -= 6
        if event.type == PIPE_SPAWN:
            pipe_list.extend(create_pipe())

    screen.blit(background_surface, (0, 0))

    # Bird
    BIRD_MOVEMENT += GRAVITY
    bird_rect.centery += BIRD_MOVEMENT
    rotated_bird = rotate_bird(bird_surface)
    screen.blit(rotated_bird, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    if not check_collision(pipe_list):
        running = False

    pygame.display.update()
    clock.tick(120)
