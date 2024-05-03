import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.dead = False
        self.scale = 0.08
        self.on_ground = True
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.original_img = pygame.image.load(f'imgs/characters/{img}.png')
        self.jumping_img = pygame.image.load(f'imgs/characters/{img}_jump.png')
        self.rect = self.original_img.get_rect()
        self.image = self.transform_image(self.original_img)
        self.img_width = self.image.get_width()
        self.img_height = self.image.get_height()
        self.rect.center = (150, 600)

    def transform_image(self, img, flip=False):
        img = pygame.transform.flip(img, flip, False)
        scaled_img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        self.rect.size = scaled_img.get_size()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        return scaled_img

    def update_image(self, keys, move_keys):
        if keys[move_keys['left']]: 
            if not self.on_ground: 
                img = self.jumping_img
            else:
                img = self.original_img
            flip = True
            self.image = self.transform_image(img, flip)

    def listen_to_movement(self, keys, move_keys):
        if keys[move_keys['left']]:
            self.moving_left = True
        if keys[move_keys['right']]:
            self.moving_right = True
            self.image = self.transform_image(self.original_img)
        if keys[move_keys['up']]:
            self.jump = True


    def check_collisions(self, platforms): 
        print(self.rect)
        for platform in platforms:
            # collision_occur = self.rect.colliderect(platform)
            # print(collision_occur)
            if self.moving_right and platform.colliderect(self.rect.x + 3, self.rect.y, self.rect.width, self.rect.height):
                self.moving_right = False
            if self.moving_left and platform.colliderect(self.rect.x - 3, self.rect.y, self.rect.width, self.rect.height):
                self.moving_left = False
            if self.jumping:
                self.jumping = False
                self.on_ground = False
                
    def update_position(self):
        if self.moving_right:
            self.rect.x += 3
        if self.moving_left:
            self.rect.x -= 3
        if self.jumping:
            self.rect.y -= 3

    # def apply_gravity(self):
    #     if not self.on_ground:
    #         self.rect.y += 1

    def move(self, move_keys, platforms): 
        keys = pygame.key.get_pressed()
        self.listen_to_movement(keys, move_keys)
        self.update_image(keys, move_keys)
        self.check_collisions(platforms)
        self.update_position()
        # self.apply_gravity()
        
