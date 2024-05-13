import pygame

# NOT MY CODE. COPIED FROM THE INTERNET
# However, I understand the code now after working with it for a while

class Button():
    def __init__(self, x, y, image, scale, id):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.id = id

    # "draw" function draws the literal button and checks if its clicked
    def draw(self, surface):
        action = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # if mouse is over the button and collides, clicked is True and "action" has been preformed
        if self.rect.collidepoint(pos):
            # This code: "pygame.mouse.get_pressed()[0] == 1" checks if the left mouse button has been pressed
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                action = True
                self.clicked = True

        # if player right clicks, don't select button
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draws the button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # returns True when a button is clicked
        return action
