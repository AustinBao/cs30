import pygame
import os
import player
import button
import time


pygame.init()

# https://www.youtube.com/watch?v=ST-Qq3WBZBE
# https://www.youtube.com/watch?v=xYhniILN6Ls
# https://stackoverflow.com/questions/74978204/how-to-draw-a-dashed-line-in-python-using-pygame

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800

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
isItemChosen = False
isItemsPlaced = False
isPlayerOneItemPlaced = False
isPlayerTwoItemPlaced = False
item_being_placed = None  # Track the item ID currently being placed
item_placement_pending = False  # True if an item is selected but not placed
current_tile = 0
number_of_players = 2
selected_items = []
TILE_SIZE_MAIN = 100
TILE_SIZE_SMALL = TILE_SIZE_MAIN // 4
MAIN_ROWS = SCREEN_HEIGHT // TILE_SIZE_MAIN
MAIN_COLS = SCREEN_WIDTH // TILE_SIZE_MAIN
SMALL_ROWS = SCREEN_HEIGHT // TILE_SIZE_SMALL
SMALL_COLS = SCREEN_WIDTH // TILE_SIZE_SMALL
PREGAME_WIDTH = 700
PREGAME_HEIGHT = 600
START_PREGAME_X = (SCREEN_WIDTH - PREGAME_WIDTH) // 2
START_PREGAME_Y = (SCREEN_HEIGHT - PREGAME_HEIGHT) // 2

# place items are all scaled to match the grid
place_item_list = []
number_of_items = len(os.listdir('imgs/items')) - 1
for i in range(number_of_items):
	img = pygame.image.load(f'imgs/items/{i}.png')
	if i == 5:
		scaled_img = pygame.transform.scale(img, (TILE_SIZE_MAIN//2, TILE_SIZE_MAIN//2))
	else:
		scaled_img = pygame.transform.scale_by(img, 0.7)
	place_item_list.append(scaled_img)

# convert imgs into button objects
button_list = []
button_col = 0
for i in range(len(place_item_list)):
	tile_button = button.Button(START_PREGAME_X + (button_col * 120) + 20 , START_PREGAME_Y + 150 , place_item_list[i], 1, i)
	button_list.append(tile_button)
	button_col += 1
		
# Empty tile list
world_data = []
for row in range(SMALL_ROWS):
	r = [-1] * SMALL_COLS
	world_data.append(r)

# Load player
player1_keys = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}
player2_keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}

racoon = player.Player(150, 600, 0.08, "rac", world_data) # player 1
iguana = player.Player(140, 600, 0.08, "ig", world_data) # player 2

background = pygame.image.load("imgs/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bkg():
	screen.fill(WHITE)
	screen.blit(background, (0, 0))

def draw_main_grid():
	#vertical lines
	for c in range(MAIN_COLS + 1):
		pygame.draw.line(screen, BLUE, (c * TILE_SIZE_MAIN, 0), (c * TILE_SIZE_MAIN, SCREEN_HEIGHT), 3)
	#horizontal lines
	for r in range(MAIN_ROWS + 1):
		pygame.draw.line(screen, BLUE, (0, r * TILE_SIZE_MAIN), (SCREEN_WIDTH, r * TILE_SIZE_MAIN), 3)


def draw_smaller_grid():
	#vertical lines
	for c in range(SMALL_COLS + 1):
		pygame.draw.line(screen, LIGHTBLUE, (c * TILE_SIZE_SMALL, 0), (c * TILE_SIZE_SMALL, SCREEN_HEIGHT), 3)
	#horizontal lines
	for r in range(SMALL_ROWS + 1):
		pygame.draw.line(screen, LIGHTBLUE, (0, r * TILE_SIZE_SMALL), (SCREEN_WIDTH, r *TILE_SIZE_SMALL), 3)


def draw_player(self, screen):
    screen.blit(self.image, (self.x, self.y))


def draw_pre_game():
	pygame.draw.rect(screen, CARDBOARD, pygame.Rect(START_PREGAME_X, START_PREGAME_Y, PREGAME_WIDTH, PREGAME_HEIGHT))
	
def draw_world():
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				img = pygame.image.load(f'imgs/items/{tile}.png')
				img = pygame.transform.scale(img, (TILE_SIZE_SMALL + 4,TILE_SIZE_SMALL + 4))
				screen.blit(img, (x * TILE_SIZE_SMALL, y * TILE_SIZE_SMALL))

def placeitem(id, x, y):
	if 0 <= x < SMALL_COLS and 0 <= y < SMALL_ROWS:
		if id == 1 or id == 3:
			for i in range(4):
				world_data[y - i][x] = id
		else:
			world_data[y][x] = id
		print("Updated world_data at ({}, {}):".format(y, x))

def scaleitem(item, img):
	if item == 1 or item == 3: 
		return pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_MAIN))
	else:
		return pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_SMALL))

run = True
while run:
	pos = pygame.mouse.get_pos()
	x = pos[0] // TILE_SIZE_SMALL
	y = pos[1] // TILE_SIZE_SMALL

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if item_placement_pending and 0 <= x < SMALL_COLS and 0 <= y < SMALL_ROWS:
                # Place the item at the cursor position
				placeitem(item_being_placed, x, y)
				item_being_placed = None
				item_placement_pending = False
				
				# Automatically load the next item if available
				if len(selected_items) > 0:
					item_being_placed = selected_items.pop(0)
					item_placement_pending = True
				else:
					isItemChosen = False
					isItemsPlaced = True

	if isPregameOpen:
		draw_bkg() 
		draw_pre_game()
		for b in button_list:
			if b.draw(screen):
				selected_items.append(b.id)
				if len(selected_items) == number_of_players:
					item_being_placed = selected_items.pop(0)
					item_placement_pending = True
					isPregameOpen = False
					isItemChosen = True
	
	if isItemChosen:
		draw_bkg()
		draw_smaller_grid()
		draw_main_grid()

		if item_placement_pending:
			img = pygame.image.load(f'imgs/items/{item_being_placed}.png')
			img = scaleitem(item_being_placed, img)
			img.set_alpha(128)
			screen.blit(img, (pos[0] - img.get_width() // 2, pos[1] - img.get_height() // 2))

		draw_world()

	if isItemsPlaced:
		draw_bkg()
		draw_world()
		draw_player(racoon, screen)
		draw_player(iguana, screen)
		racoon.move(player1_keys)
		iguana.move(player2_keys)
	

	pygame.display.update()

pygame.quit()

