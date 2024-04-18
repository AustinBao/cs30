import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, scale, img):
        pygame.sprite.Sprite.__init__(self)
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.on_ground = False
        self.gravity = 0.7
        self.scale = scale
        self.image = self.transform_image(self.original_img)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def transform_image(self, img, flip=False):
        img = pygame.transform.flip(img, flip, False)
        return pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))

    def update_image(self, keys, move_keys):
        if keys[move_keys['left']]:
            if self.on_ground:
                img = self.original_img
            else:
                img = self.jumping_img
            flip = True
            self.image = self.transform_image(img, flip)


    def update_position(self, keys, move_keys):
        dx, dy = 0, 0

        if keys[move_keys['left']]:
            dx -= 3
        if keys[move_keys['right']]:
            self.image = self.transform_image(self.original_img)
            dx += 3
        if keys[move_keys['up']] and self.on_ground:
            self.on_ground = False
            dy -= 10

        self.y += dy
        self.x += dx

# NOT MY CODE
    def platform_collision(self, platforms):
        # Horizontal Collision
        self.x += self.x_vel
        collided_platform_index = self.rect.collidelist(platforms)
        if collided_platform_index >= 0:
            collided_platform = platforms[collided_platform_index]
            if self.x_vel > 0:
                self.rect.right = collided_platform.left
                self.x_vel = 0
            elif self.x_vel < 0:
                self.rect.left = collided_platform.right
                self.x_vel = 0
        self.x -= self.x_vel

        # Vertical Collision
        self.y += self.y_vel
        collided_platform_index = self.rect.collidelist(platforms)
        if collided_platform_index >= 0:
            collided_platform = platforms[collided_platform_index]
            if self.y_vel > 0:
                self.rect.bottom = collided_platform.top
                self.y_vel = 0
                self.on_ground = True
            elif self.y_vel < 0:
                self.rect.top = collided_platform.bottom
                self.y_vel = 0
        else:
            self.on_ground = False
        self.y -= self.y_vel

    def apply_gravity(self):
        self.y_vel = min(self.y_vel + self.gravity, 30)

    def move(self, move_keys, platforms): 
        keys = pygame.key.get_pressed()
        self.update_position(keys, move_keys)
        self.update_image(keys, move_keys)
        self.platform_collision(platforms)
        self.apply_gravity()
