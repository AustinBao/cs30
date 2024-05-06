

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, name, img):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.dead = False
        self.scale = 0.08
        self.on_ground = False
        self.jumping = False
        self.gravity = 1
        self.jump_height = -15
        self.y_velocity = self.jump_height
        self.moving_left = False
        self.moving_right = False
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.rect = self.original_img.get_rect()
        self.image = self.transform_image(self.original_img)
        self.img_width = self.image.get_width()
        self.img_height = self.image.get_height()
        self.rect.center = (150, 600)

    def reset_player(self):
        self.rect.center = (150, 600)
        self.dead = False
    def dead_to_border(self):
        #  Check if player touches the bottom of the map
        if self.rect.y + self.img_height > 800:
            self.dead = True
    def transform_image(self, img, flip=False):
        img = pygame.transform.flip(img, flip, False)
        scaled_img = pygame.transform.scale(img,
                                            (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect.size = scaled_img.get_size()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        return scaled_img






    def check_collisions(self, platforms, dx, dy):
        for platform, platforms_id in platforms:
            # Horizontal movement
            if platform.colliderect(self.rect.x + dx, self.rect.y, self.img_width, self.img_height):
                dx = 0

            # Vertical movement
            if platform.colliderect(self.rect.x, self.rect.y + dy, self.img_width, self.img_height):
                if self.y_velocity < 0:
                    self.y_velocity = 0
                    dy = platform.bottom - self.rect.top

                if self.y_velocity >= 0:
                    self.y_velocity = 0
                    dy = platform.top - self.rect.bottom

        self.rect.x += dx
        self.rect.y += dy

    def listen_to_movement(self, keys, move_keys, platforms):
        dx, dy = 0, 0
        if keys[move_keys['left']]:
            dx -= 3
            self.moving_left = True
            self.moving_right = False
        if keys[move_keys['right']]:
            dx += 3
            self.moving_right = True
            self.moving_left = False
        if keys[move_keys['up']] and self.on_ground:
            dy += self.jump_height
            self.jumping = True
            self.on_ground = False
        self.check_collisions(platforms, dx, dy)

    def handle_jumping(self):
        # Watched a Youtube tutorial for the jumping logic: https://www.youtube.com/watch?v=ST-Qq3WBZBE&t=325s
        if self.jumping:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.on_ground = True
                self.y_velocity = self.jump_height
            #  if moving left, flip the jumping image
            if self.moving_left:
                self.image = self.transform_image(self.jumping_img, True)
            else:
                self.image = self.transform_image(self.jumping_img)
        # if not jumping, keep standing image and flip according to direction of movement
        else:
            if self.moving_left:
                self.image = self.transform_image(self.original_img, True)
            else:
                self.image = self.transform_image(self.original_img)

    def apply_gravity(self):
        # check if jumping in order to not shift the player too much (jumping already has gravity)
        if not self.jumping:
            if not self.on_ground:
                self.rect.y += self.gravity

    def move(self, move_keys, platforms):
        keys = pygame.key.get_pressed()
        self.listen_to_movement(keys, move_keys, platforms)
        self.handle_jumping()
        self.dead_to_border()
        self.apply_gravity()
