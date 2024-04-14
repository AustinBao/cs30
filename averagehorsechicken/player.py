import pygame

class Player(pygame.sprite.Sprite):
    Y_GRAVITY = 0.14
    JUMP_HEIGHT = 7
    Y_VELOCITY = JUMP_HEIGHT

    def __init__(self, x, y, scale, img):
        pygame.sprite.Sprite.__init__(self)
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.scale = scale
        self.x = x
        self.y = y
        self.jumping = False
        self.image = self.transform_image(self.original_img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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

    def update_position(self, keys, move_keys):
        if keys[move_keys['left']]:
            self.x -= 3
        if keys[move_keys['right']]:
            self.x += 3
        if keys[move_keys['up']]:
            self.jumping = True
        if keys[move_keys['down']]:
            self.y += 3

    def handle_jumping(self):
        if self.jumping:
            self.y -= Player.Y_VELOCITY
            Player.Y_VELOCITY -= Player.Y_GRAVITY
            if Player.Y_VELOCITY < -Player.JUMP_HEIGHT:
                self.jumping = False
                Player.Y_VELOCITY = Player.JUMP_HEIGHT

    def move(self, move_keys):
        keys = pygame.key.get_pressed()
        self.update_position(keys, move_keys)
        self.update_image(keys, move_keys)
        self.handle_jumping()
        self.rect.center = (self.x, self.y)
