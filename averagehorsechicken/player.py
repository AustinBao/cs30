import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, name, img):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.dead = False
        self.scale = 0.08
        self.on_ground = True
        self.jumping = False
        self.can_jump = True
        self.gravity = 2
        self.jump_height = 20
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

    def transform_image(self, img, flip=False):
        img = pygame.transform.flip(img, flip, False)
        scaled_img = pygame.transform.scale(img,
                                            (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect.size = scaled_img.get_size()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        return scaled_img

    def check_collision_x(self, platforms, dx):
        for platform, platforms_id in platforms:
            if platform.colliderect(self.rect.x + dx, self.rect.y, self.img_width, self.img_height):
                dx = 0
        self.rect.x += dx

    def check_collision_y(self, platforms, dy):
        collision = False
        for platform, platforms_id in platforms:
            if platform.colliderect(self.rect.x, self.rect.y + dy, self.img_width, self.img_height):
                collision = True
                if dy < 0:  # Moving up
                    self.rect.top = platform.bottom
                    self.y_velocity = 0  # Stop upward movement
                elif dy > 0:  # Moving down
                    self.rect.bottom = platform.top
                    self.y_velocity = 0  # Stop downward movement
                    self.on_ground = True
                    self.jumping = False
                break
        return collision

    def listen_to_movement(self, keys, move_keys, platforms):
        dx = 0
        if keys[move_keys['left']]:
            dx -= 3
            self.moving_left = True
            self.moving_right = False
        elif keys[move_keys['right']]:
            dx += 3
            self.moving_right = True
            self.moving_left = False
        else:
            self.moving_left = False
            self.moving_right = False

        if keys[move_keys['up']] and self.on_ground and self.can_jump:
            self.jumping = True
            self.can_jump = False
            self.on_ground = False
            self.y_velocity = -self.jump_height

        self.check_collision_x(platforms, dx)


    def check_on_ground(self, platforms):
        self.rect.y += 1
        on_ground = False
        for platform, platform_id in platforms:
            if self.rect.colliderect(platform):
                self.dead = platform_id in [3, 4]
                on_ground = True
                self.can_jump = True
                break
        self.rect.y -= 1
        return on_ground

    def handle_jumping(self, platforms):
        if self.jumping:
            new_y = self.rect.y + self.y_velocity  # Should be adding velocity because it starts negative
            collided = self.check_collision_y(platforms, self.y_velocity)
            if not collided:
                self.rect.y = new_y
            self.y_velocity += self.gravity  # Gravity should increment to bring the velocity towards zero and positive
            if self.y_velocity >= 0:  # When velocity reaches zero, the peak of the jump has been reached
                self.jumping = False

    def apply_gravity(self):
        # check if jumping in order to not shift the player too much (jumping already has gravity)
        if not self.jumping and not self.on_ground:
            self.rect.y += self.gravity

    def dead_to_border(self):
        #  Check if player touches the bottom of the map
        if self.rect.y + self.img_height > 800:
            self.dead = True

    def move(self, move_keys, platforms):
        keys = pygame.key.get_pressed()
        self.listen_to_movement(keys, move_keys, platforms)
        self.handle_jumping(platforms)
        self.on_ground = self.check_on_ground(platforms)
        self.apply_gravity()
        self.dead_to_border()

