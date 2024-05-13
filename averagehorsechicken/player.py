import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, name, img):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.dead = False
        self.scale = 0.08
        self.on_ground = False
        self.jumping = False
        self.can_jump = True
        self.gravity = 2
        self.jump_height = 20
        self.y_velocity = self.jump_height
        self.moving_right = False
        self.moving_left = False
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.rect = self.original_img.get_rect()
        self.image = self.transform_image(self.original_img)
        self.img_width = self.image.get_width()
        self.img_height = self.image.get_height()
        self.rect.center = (150, 600)

    def reset_player(self):
        # move player back to spawn
        self.rect.center = (150, 600)
        self.dead = False

    def transform_image(self, img, flip=False):
        # scales and flips image. Provides the center of the player as well.
        img = pygame.transform.flip(img, flip, False)
        scaled_img = pygame.transform.scale(img,(25, 25))
        self.rect.size = scaled_img.get_size()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        return scaled_img

    def orientation_while_jump(self):
        # Makes sure the player image is facing the right direction when jumping
        if self.moving_left:
            self.image = self.transform_image(self.jumping_img, True)
        elif self.moving_right:
            self.image = self.transform_image(self.jumping_img)

    def orientation_while_grounded(self):
        # Makes sure the player image is facing the right direction when stationary on the ground
        if self.moving_left:
            self.image = self.transform_image(self.original_img, True)
        elif self.moving_right:
            self.image = self.transform_image(self.original_img)

    def check_collision_x(self, platforms, dx):
        # iterate through platforms list to check which platforms collide with the player
        for platform, platform_id in platforms:
            # future_rect checks if the move WERE TO HAPPEN would it collide with anything?
            future_rect = pygame.Rect(self.rect.x + dx, self.rect.y, self.img_width, self.img_height)
            if future_rect.colliderect(platform):
                # if the player touches barbwire they die (ids 3 and 4)
                self.dead = platform_id in [3, 4]
                return 0
        return dx

    def check_collision_y(self, platforms, dy):
        collision = False
        # iterate through platforms list to check which platforms collide with the player
        for platform, platforms_id in platforms:
            # future_rect checks if the move WERE TO HAPPEN would it collide with anything?
            future_rect = pygame.Rect(self.rect.x, self.rect.y + dy, self.img_width, self.img_height)
            if future_rect.colliderect(platform):
                collision = True
                if dy < 0:  # Moving up; player hitting their head on a platform's bottom
                    self.rect.top = platform.bottom
                    self.y_velocity = 0
                elif dy > 0:  # Moving down; falling onto a platform, therefore reset on_ground and jumping
                    self.rect.bottom = platform.top
                    self.y_velocity = 0
                    self.on_ground = True
                    self.jumping = False
                break
        return collision

    def listen_to_movement(self, keys, move_keys, platforms):
        # dx represents the potential movement left or right
        dx = 0
        # Check both player's respective keybinds by using their keys in the dictionary
        if keys[move_keys['left']]:
            dx -= 3
            self.moving_right = False
            self.moving_left = True
            # flips image when moving left since original_img is right facing
            self.image = self.transform_image(self.original_img, True)

        elif keys[move_keys['right']]:
            dx += 3
            self.moving_right = True
            self.moving_left = False
            self.image = self.transform_image(self.original_img)

        # dx becomes 0 if there is a collision in the x direction
        dx = self.check_collision_x(platforms, dx)
        self.rect.x += dx

        if keys[move_keys['up']] and self.on_ground and self.can_jump:
            self.jumping = True
            self.can_jump = False
            self.on_ground = False
            self.y_velocity = -self.jump_height

    def check_on_ground(self, platforms):
        # Test if on ground by moving player down by one and checking for collision
        self.rect.y += 1
        on_ground = False
        for platform, platform_id in platforms:
            # Reset can_jump and other player variables if on ground
            if self.rect.colliderect(platform):
                # Specific platform ids that cause death (barbwire platforms)
                self.dead = platform_id in [3, 4]
                on_ground = True
                self.can_jump = True
                self.orientation_while_grounded()
                break
        # Revert original test move
        self.rect.y -= 1
        return on_ground

    def handle_jumping(self, platforms):
        if self.jumping:
            self.orientation_while_jump()
            new_y = self.rect.y + self.y_velocity
            # checks for vertical collision
            collided = self.check_collision_y(platforms, self.y_velocity)
            if not collided:
                self.rect.y = new_y
            # Gravity should increment to bring the velocity towards zero and positive
            self.y_velocity += self.gravity
            # When the y_velocity reaches zero, the peak of the jump has been reached
            if self.y_velocity >= 0:
                self.jumping = False

    def apply_gravity(self):
        # check if jumping in order to not shift the player too much as jumping already includes gravity
        if not self.jumping and not self.on_ground:
            self.rect.y += self.gravity

    def dead_to_border(self):
        #  Check if player touches the bottom of the map. If so, they die
        if self.rect.y + self.img_height > 800:
            self.dead = True

    # Handles all the player's movements
    def move(self, move_keys, platforms):
        keys = pygame.key.get_pressed()
        self.apply_gravity()
        self.listen_to_movement(keys, move_keys, platforms)
        self.handle_jumping(platforms)
        self.on_ground = self.check_on_ground(platforms)
        self.dead_to_border()
