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
        self.gravity = 1
        self.jump_height = 15
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
        scaled_img = pygame.transform.scale(img,(int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect.size = scaled_img.get_size()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        return scaled_img

    def check_collisions(self, platforms, dx, dy):
        horizontal_collision = False
        vertical_collision = False

        # Create rectangles for the character's current and updated positions
        current_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        updated_rect = pygame.Rect(self.rect.x + dx, self.rect.y + dy, self.rect.width, self.rect.height)

        # Check for collisions with platforms
        for platform, platform_id in platforms:
            if updated_rect.colliderect(platform):
                # Handle horizontal collision
                if dx > 0:
                    current_rect.right = platform.left
                    horizontal_collision = True
                elif dx < 0:
                    current_rect.left = platform.right
                    horizontal_collision = True

                # Handle vertical collision
                if dy > 0:
                    current_rect.bottom = platform.top
                    vertical_collision = True
                elif dy < 0:
                    current_rect.top = platform.bottom
                    vertical_collision = True

        # Update position based on collisions
        if not horizontal_collision:
            self.rect.x += dx
        if not vertical_collision:
            self.rect.y += dy

        # Adjust vertical movement if there's a horizontal collision while jumping
        if self.jumping and horizontal_collision and not vertical_collision:
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
        if keys[move_keys['up']] and self.on_ground and self.can_jump:
            dy -= self.jump_height
            self.jumping = True
            self.can_jump = False
            self.on_ground = False

        self.check_collisions(platforms, dx, dy)

    def check_on_ground(self, platforms):
        self.rect.y += 1
        on_ground = False
        for platform, platform_id in platforms:
            if self.rect.colliderect(platform):
                if platform_id == 3 or platform_id == 4:
                    self.dead = True
                on_ground = True
                self.can_jump = True
                break
        self.rect.y -= 1
        return on_ground

    def handle_jumping(self):
        if self.jumping:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.on_ground = True
                self.y_velocity = self.jump_height
            if self.moving_left:
                self.image = self.transform_image(self.jumping_img, True)
            else:
                self.image = self.transform_image(self.jumping_img)
        else:
            if self.moving_left:
                self.image = self.transform_image(self.original_img, True)
            else:
                self.image = self.transform_image(self.original_img)

    def apply_gravity(self):
        if not self.jumping:
            if not self.on_ground:
                self.rect.y += self.gravity
            if self.rect.y + self.img_height > 800:
                self.dead = True

    def move(self, move_keys, platforms):
        keys = pygame.key.get_pressed()
        self.listen_to_movement(keys, move_keys, platforms)
        self.on_ground = self.check_on_ground(platforms)
        self.handle_jumping()
        self.apply_gravity()
