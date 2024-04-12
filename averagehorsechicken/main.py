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
isPlaceItemOpen = True
current_tile = 0
number_of_players = 1
TILE_SIZE = 100 
MAIN_ROWS = SCREEN_HEIGHT // TILE_SIZE
MAIN_COLS = SCREEN_WIDTH // TILE_SIZE
SMALL_ROWS = SCREEN_HEIGHT // 4
SMALL_COLS = SCREEN_WIDTH // 4
PREGAME_WIDTH = 700
PREGAME_HEIGHT = 600
START_PREGAME_X = (SCREEN_WIDTH - PREGAME_WIDTH) // 2
START_PREGAME_Y = (SCREEN_HEIGHT - PREGAME_HEIGHT) // 2


# Load player
racoon = player.Player(150, 600, 0.08, "rac.png")

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
# place items are all scaled to match the grid
place_item_list = []
number_of_items = len(os.listdir('imgs/items')) - 1
for i in range(number_of_items):
	img = pygame.image.load(f'imgs/items/{i}.png')
	scaled_img = pygame.transform.scale_by(img, 0.7)
	place_item_list.append(scaled_img)

# convert imgs into button objects
button_list = []
button_col = 0
for i in range(len(place_item_list)):
	tile_button = button.Button(START_PREGAME_X + (button_col * 130) + 50, START_PREGAME_Y + 150 , place_item_list[i], 1, i)
	button_list.append(tile_button)
	button_col += 1
		


def draw_pre_game():
	pygame.draw.rect(screen, CARDBOARD, pygame.Rect(START_PREGAME_X, START_PREGAME_Y, PREGAME_WIDTH, PREGAME_HEIGHT))
	

run = True
while run:

	if isPregameOpen:
		draw_bkg()
		draw_pre_game()
		selected_items = []
		for current_count, b in enumerate(button_list):
			if b.draw(screen):
				selected_items.append(b.id)
				print(selected_items)
				if len(selected_items) == number_of_players:
					isPregameOpen = False
	else:
		if isPlaceItemOpen:
			draw_bkg()
			draw_smaller_grid()
			draw_main_grid()
			pos = pygame.mouse.get_pos()
			for items in selected_items:
				img = pygame.image.load(f'imgs/items/{items}.png')
				# If the items are long vertical items, scale differently
				if items == 1 or items == 3: 
					img = pygame.transform.scale(img, (25, TILE_SIZE))
				# If items is crossbow
				elif items == 0:
					img = pygame.transform.scale(img, (25, TILE_SIZE//2))
				# If items are one tile 
				else:
					img = pygame.transform.scale(img, (25, 25))
				img.set_alpha(128)
				screen.blit(img, (pos[0] - img.get_width(), pos[1] - img.get_height()))
			
		else:
			draw_player(racoon, screen)
			racoon.move()	
			
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			run = False

	
	pygame.display.update()

pygame.quit()

