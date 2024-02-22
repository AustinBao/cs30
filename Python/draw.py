import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Platform")


def drawrect(canvas, color1, color2, x1 , y1, x2, y2, width, height):
    pygame.draw.rect(canvas, color2, pygame.Rect(x1, y1, x2 + width, y2 + height))
    pygame.draw.rect(canvas, color1, pygame.Rect(x1, y1 + 10,  x2 + width , y2 + height))


# Main loop
while True:
    screen.fill((255, 255, 255)) 
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    
    # Drawing Rectangle    
    drawrect(screen, (255,0,0), (0,255,0), 30, 30, 60, 60, 100, 10)
    drawrect(screen, (255,0,0), (0,255,0), 160, 160, 20, 20, 400, 5)
    drawrect(screen, (139,69,19), (128,0,0), 300, 300, 100, 100, 300, 1)

    
    # Update the display
    pygame.display.flip()

