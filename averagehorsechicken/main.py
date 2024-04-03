import pygame

pygame.init()

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
#define game variables
TILE_SIZE = 100
MAIN_ROWS = SCREEN_HEIGHT // TILE_SIZE
MAIN_COLS = SCREEN_WIDTH // TILE_SIZE

SMALL_ROWS = SCREEN_HEIGHT // 4
SMALL_COLS = SCREEN_WIDTH // 4

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


run = True
while run:
	
	draw_bkg()
	draw_smaller_grid()
	draw_main_grid()

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()

