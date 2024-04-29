import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.scale = 0.08
        self.gravity = 5
        self.on_ground = False
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
        self.rect.x += dx
        self.rect.y += dy

    # def apply_gravity(self):
    #     if not self.on_ground:
    #         self.rect.bottom += self.gravity
    
    def check_collisions(self, platforms):
        collide_index = self.rect.collidelistall(platforms)
        print(collide_index)
        # collide = pygame.Rect.colliderect(self.rect, player_rect2)
    
    def move(self, move_keys, platforms): 
        keys = pygame.key.get_pressed()
        self.update_position(keys, move_keys)
        self.update_image(keys, move_keys)
        self.check_collisions(platforms)
        # self.apply_gravity()
        
