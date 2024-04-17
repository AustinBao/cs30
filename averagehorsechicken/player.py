import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, scale, img):
        pygame.sprite.Sprite.__init__(self)
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.scale = scale
        self.x = x
        self.y = y
        self.JUMP_HEIGHT = 10
        self.Y_GRAVITY = 0.3
        self.jumping = False
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.image = self.transform_image(self.original_img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def transform_image(self, img, flip=False):
        img = pygame.transform.flip(img, flip, False)
        return pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))

    def update_image(self, keys, move_keys):
        if self.jumping:
            img = self.jumping_img
            # flip becomes true when turning left thus flipping the image
            flip = keys[move_keys['left']]
        else:
            img = self.original_img
            flip = keys[move_keys['left']] and not keys[move_keys['right']]
        self.image = self.transform_image(img, flip)

    # def on_ground(self):
    #     return not self.can_move_to(self.x, self.y + self.height + 1)

    # def can_move_to(self, x, y):


    def update_position(self, keys, move_keys):
        dx, dy = 0, 0

        if keys[move_keys['left']]:
            dx -= 3
        if keys[move_keys['right']]:
            dx += 3
        if keys[move_keys['up']]:
            self.jumping = True
        if keys[move_keys['down']]:
            dy += 3



    # def handle_jumping(self, keys, move_keys):
    #     if keys[move_keys['up']] and self.on_ground():
    #         self.jumping = True

    #     if self.jumping:
    #         self.Y_VELOCITY -= self.Y_GRAVITY
    #         if self.Y_VELOCITY < -self.JUMP_HEIGHT:
    #             self.jumping = False  


    def move(self, move_keys):
        keys = pygame.key.get_pressed()
        self.update_position(keys, move_keys)
        self.update_image(keys, move_keys)
        self.handle_jumping(keys, move_keys)
        self.rect.center = (self.x, self.y)
