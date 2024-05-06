#                        ***** INSTRUCTIONS TO PLAY *****
#   - The goal is to reach the red flag at the top. The first one to touch it wins.
#   - There are initially NO tiles for you to stand on (even the spawn area). The point is to make your own path.
#   - However, your opponent can try to stop your path by obstructing it using tiles.
#   - If you happen trap yourself and there is no way out, click the restart button in the bottom right.


import pygame
import os
import player
import button
import crossbow

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Average Horse Chicken')

# define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
BLACK = (0, 0, 0)
BLUE = (111, 143, 175)
LIGHTBLUE = (173, 216, 230)
CARDBOARD = (159, 135, 103)

# define game variables/states
isPregameOpen = True
isItemChosen = False
isItemsPlaced = False
isPlayerOneItemPlaced = False
isPlayerTwoItemPlaced = False
isGameOver = False
# Track the item ID currently being placed
item_being_placed = None
# True if an item is selected but not placed
item_placement_pending = False
current_tile = 0
number_of_players = 2
selected_items = []
platforms = []
crossbows = []
font = pygame.font.Font(None, 64)
flag = pygame.Rect(125, 150, 25, 25)

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

# Load player and give them their traits(movement keys and name)
player1_keys = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}
player2_keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}

player1_name = "Austin"
player2_name = "Bob"

racoon = player.Player(player1_name, "rac")
iguana = player.Player(player2_name, "ig")

background = pygame.image.load("imgs/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# place items are all scaled to match the grid
place_item_list = []
number_of_items = len(os.listdir('imgs/items')) - 1
for i in range(number_of_items):
    img = pygame.image.load(f'imgs/items/{i}.png')
    # solely target and scale the last item since the png is enormous
    if i == 5:
        scaled_img = pygame.transform.scale(img, (TILE_SIZE_MAIN // 2, TILE_SIZE_MAIN // 2))
    else:
        scaled_img = pygame.transform.scale_by(img, 0.7)
    place_item_list.append(scaled_img)

# convert imgs into button objects
button_list = []
button_col = 0
for i in range(len(place_item_list)):
    tile_button = button.Button(START_PREGAME_X + (button_col * 120) + 20, START_PREGAME_Y + 150, place_item_list[i], 1,
                                i)
    button_list.append(tile_button)
    button_col += 1


def generate_empty_world_data():
    data = []
    for row in range(SMALL_ROWS):
        r = [-1] * SMALL_COLS
        data.append(r)
    return data


# Empty tile list which represents the grid
world_data = generate_empty_world_data()


def draw_bkg():
    screen.fill(WHITE)
    screen.blit(background, (0, 0))


def draw_main_grid():
    # LARGE vertical lines
    for c in range(MAIN_COLS + 1):
        pygame.draw.line(screen, BLUE, (c * TILE_SIZE_MAIN, 0), (c * TILE_SIZE_MAIN, SCREEN_HEIGHT), 3)
    # LARGE horizontal lines
    for r in range(MAIN_ROWS + 1):
        pygame.draw.line(screen, BLUE, (0, r * TILE_SIZE_MAIN), (SCREEN_WIDTH, r * TILE_SIZE_MAIN), 3)


def draw_smaller_grid():
    # SMALL vertical lines
    for c in range(SMALL_COLS + 1):
        pygame.draw.line(screen, LIGHTBLUE, (c * TILE_SIZE_SMALL, 0), (c * TILE_SIZE_SMALL, SCREEN_HEIGHT), 3)
    # SMALL horizontal lines
    for r in range(SMALL_ROWS + 1):
        pygame.draw.line(screen, LIGHTBLUE, (0, r * TILE_SIZE_SMALL), (SCREEN_WIDTH, r * TILE_SIZE_SMALL), 3)


def draw_player(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))


def draw_pre_game():
    # Only draws the background
    pygame.draw.rect(screen, CARDBOARD, pygame.Rect(START_PREGAME_X, START_PREGAME_Y, PREGAME_WIDTH, PREGAME_HEIGHT))


def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                img = pygame.image.load(f'imgs/items/{tile}.png')
                if tile == 0:
                    img = pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_MAIN // 2))
                elif tile == 1 and tile == 3:
                    img = pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_MAIN))
                else:
                    img = pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_SMALL))
                screen.blit(img, (x * TILE_SIZE_SMALL, y * TILE_SIZE_SMALL))


def placeitem(id, x, y):
    if 0 <= x < SMALL_COLS and 0 <= y < SMALL_ROWS:
        if id == 1 or id == 3:
            for i in range(4):
                world_data[y - i][x] = id
                platforms.append(
                    (pygame.Rect(x * TILE_SIZE_SMALL, (y - i) * TILE_SIZE_SMALL, TILE_SIZE_SMALL, TILE_SIZE_SMALL), id))
        elif id == 0:
            world_data[y - 1][x] = id
            new_crossbow = crossbow.Crossbow((x * TILE_SIZE_SMALL, y * TILE_SIZE_SMALL))
            crossbows.append(new_crossbow)
            platforms.append(
                (pygame.Rect(x * TILE_SIZE_SMALL, y * TILE_SIZE_SMALL, TILE_SIZE_SMALL, TILE_SIZE_SMALL), id))
        else:
            world_data[y][x] = id
            platforms.append(
                (pygame.Rect(x * TILE_SIZE_SMALL, y * TILE_SIZE_SMALL, TILE_SIZE_SMALL, TILE_SIZE_SMALL), id))
    print(platforms)


def scaleitem(item, img):
    if item == 1 or item == 3:
        return pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_MAIN))
    elif item == 0:
        return pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_MAIN // 2))
    else:
        return pygame.transform.scale(img, (TILE_SIZE_SMALL, TILE_SIZE_SMALL))


def resetround(player1, player2):
    global isPregameOpen, isItemChosen, isItemsPlaced, isPlayerOneItemPlaced, isPlayerTwoItemPlaced
    isPregameOpen = True
    isItemChosen = False
    isItemsPlaced = False
    isPlayerOneItemPlaced = False
    isPlayerTwoItemPlaced = False

    player1.reset_player()
    player2.reset_player()


def game_over(player1, player2):
    draw_bkg()
    game_over_text = font.render("Game Over", True, WHITE)
    player_who_won_text = font.render(f"{player1.name} won!", True, WHITE)

    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    player_rect = player_who_won_text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 100))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(player_who_won_text, player_rect)


def reset_game(player1, player2):
    global world_data, platforms, isGameOver
    world_data = generate_empty_world_data()
    platforms = []
    isGameOver = False
    resetround(player1, player2)


# Restart button
restart_img = pygame.image.load("imgs/restart.png")
scale = 0.3

clock = pygame.time.Clock()

run = True
while run:
    pos = pygame.mouse.get_pos()
    x = pos[0] // TILE_SIZE_SMALL
    y = pos[1] // TILE_SIZE_SMALL

    draw_bkg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if item_placement_pending and 0 <= x < SMALL_COLS and 0 <= y < SMALL_ROWS:
                # Place the item at the cursor position
                placeitem(item_being_placed, x, y)
                item_being_placed = None
                item_placement_pending = False

                if len(selected_items) > 0:
                    item_being_placed = selected_items.pop(0)
                    item_placement_pending = True
                else:
                    isItemChosen = False
                    isItemsPlaced = True

    if isPregameOpen:
        draw_pre_game()
        for b in button_list:
            if b.draw(screen):
                selected_items.append(b.id)
                if len(selected_items) == number_of_players:
                    # The first players item is selected first by pop(0)
                    item_being_placed = selected_items.pop(0)
                    item_placement_pending = True
                    isPregameOpen = False
                    isItemChosen = True

    if isItemChosen:
        draw_smaller_grid()
        draw_main_grid()
        if item_placement_pending:
            img = pygame.image.load(f'imgs/items/{item_being_placed}.png')
            img = scaleitem(item_being_placed, img)
            img.set_alpha(128)
            screen.blit(img, (pos[0] - img.get_width(), pos[1] - img.get_height()))
        draw_world()

    if isItemsPlaced:
        draw_world()
        draw_player(racoon, screen)
        draw_player(iguana, screen)

        # check if restart button is clicked
        restart_button = button.Button(SCREEN_WIDTH - (restart_img.get_width() * scale), SCREEN_HEIGHT - (restart_img.get_height() * scale), restart_img, scale, 100)
        if restart_button.draw(screen):
            reset_game(racoon, iguana)

        if len(crossbows) > 0:
            for individual_crossbow in crossbows:
                individual_crossbow.update()
                individual_crossbow.projectiles.draw(screen)

            for individual_crossbow in crossbows:
                for projectile in individual_crossbow.projectiles:
                    for platform_rect, _ in platforms:
                        if platform_rect.colliderect(projectile.rect):
                            projectile.kill()  # Remove projectile when it hits a platform
                            break
                    if racoon.rect.colliderect(projectile.rect):
                        racoon.dead = True
                        projectile.kill()
                    elif iguana.rect.colliderect(projectile.rect):
                        iguana.dead = True
                        projectile.kill()

        if not iguana.dead:
            iguana.move(player2_keys, platforms)
        if not racoon.dead:
            racoon.move(player1_keys, platforms)

        if racoon.dead and iguana.dead:
            resetround(racoon, iguana)

        if racoon.rect.colliderect(flag):
            isGameOver = True
            # Winner, Loser
            game_over(racoon, iguana)
            racoon.dead = True

        elif iguana.rect.colliderect(flag):
            isGameOver = True
            game_over(iguana, racoon)
            iguana.dead = True


    clock.tick(60)
    pygame.display.update()

pygame.quit()
