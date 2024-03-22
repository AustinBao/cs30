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

#define game variables
TILE_SIZE = 100
ROWS = SCREEN_HEIGHT // TILE_SIZE
MAX_COLS = SCREEN_WIDTH // TILE_SIZE


def draw_bkg():
	screen.fill(WHITE)

def draw_grid():
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, BLUE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT), 3)
	#horizontal lines
	for r in range(ROWS + 1):
		pygame.draw.line(screen, BLUE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE), 3)



run = True
while run:
	
	draw_bkg()
	draw_grid()

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()

