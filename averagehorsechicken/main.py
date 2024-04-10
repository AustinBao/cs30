import pygame
import os
import player
import button

pygame.init()

# https://www.youtube.com/watch?v=ST-Qq3WBZBE
# https://www.youtube.com/watch?v=xYhniILN6Ls
# https://stackoverflow.com/questions/74978204/how-to-draw-a-dashed-line-in-python-using-pygame

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor')

#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
BLACK = (0, 0, 0)
BLUE = (111, 143, 175)
LIGHTBLUE = (173, 216, 230)
CARDBOARD = (159, 135, 103)

#define game variables
isPregameOpen = True
current_tile = 0
TILE_SIZE = 100
MAIN_ROWS = SCREEN_HEIGHT // TILE_SIZE
MAIN_COLS = SCREEN_WIDTH // TILE_SIZE
SMALL_ROWS = SCREEN_HEIGHT // 4
SMALL_COLS = SCREEN_WIDTH // 4
PREGAME_WIDTH = 500
PREGAME_HEIGHT = 300
START_PREGAME_X = (SCREEN_WIDTH - PREGAME_WIDTH) // 2
START_PREGAME_Y = (SCREEN_HEIGHT - PREGAME_HEIGHT) // 2


# Load player
racoon = player.Player(200, 200, 0.1, "rac.png")

# Loading images
background = pygame.image.load("imgs/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bkg():
	screen.fill(WHITE)
	screen.blit(background, (0, 0))

def draw_main_grid():
	#vertical lines
	for c in range(MAIN_COLS + 1):
		pygame.draw.line(screen, BLUE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT), 3)
	#horizontal lines
	for r in range(MAIN_ROWS + 1):
		pygame.draw.line(screen, BLUE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE), 3)


def draw_smaller_grid():
	#vertical lines
	for c in range(SMALL_COLS + 1):
		pygame.draw.line(screen, LIGHTBLUE, (c * TILE_SIZE / 4, 0), (c * TILE_SIZE / 4, SCREEN_HEIGHT), 3)
	#horizontal lines
	for r in range(SMALL_ROWS + 1):
		pygame.draw.line(screen, LIGHTBLUE, (0, r * TILE_SIZE / 4), (SCREEN_WIDTH, r * TILE_SIZE / 4), 3)


def draw_player(self, screen):
    screen.blit(self.image, (self.x, self.y))


# load all item images for the pregame (not scaled)
pre_game_img_list = []
# place items are all scaled to match the grid
place_item_list = []
number_of_items = len(os.listdir('imgs/items'))
for i in range(number_of_items):
	img = pygame.image.load(f'imgs/items/{i}.png')
	pre_game_img = pygame.transform.scale(img, (200, 200))
	pre_game_img_list.append(pre_game_img)

	scaled_img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	place_item_list.append(scaled_img)

# convert imgs into button objects
button_list = []
button_col = 0
for i in range(len(pre_game_img_list)):
	tile_button = button.Button(START_PREGAME_X + 20 + (button_col * TILE_SIZE), START_PREGAME_Y + 60, pre_game_img_list[i], 1)
	button_list.append(tile_button)
	button_col += 1
		


def draw_pre_game():
	pygame.draw.rect(screen, CARDBOARD, pygame.Rect(START_PREGAME_X, START_PREGAME_Y, PREGAME_WIDTH, PREGAME_HEIGHT))
	

run = True
while run:

	draw_bkg()
	draw_smaller_grid()
	draw_main_grid()
	draw_pre_game()

	button_count = 0
	for current_count, b in enumerate(button_list):
		if b.draw(screen):
			current_tile = button_count
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			run = False
	
	racoon.move()

	draw_player(racoon, screen)

	pygame.display.update()
	CLOCK.tick(60)

pygame.quit()

