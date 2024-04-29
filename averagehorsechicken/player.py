import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.scale = 0.08
        self.player_y_momentum = 0
        self.air_timer = 0
        self.moving_right = False
        self.moving_left = False
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
            img = self.original_img

            if keys[move_keys['up']]:
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
        if keys[move_keys['up']]:
            if self.air_timer < 6:
                self.player_y_momentum = -5
            
        self.rect.x += dx
        self.rect.y += dy

    def check_collisions(self, keys, move_keys, platforms):
        print(self.rect)
        print(self.rect.collidelistall(platforms))
    # def collision_test(rect, tiles):
    #     hit_list = []
    #     for tile in tiles:
    #         if rect.colliderect(tile):
    #             hit_list.append(tile)
    #     return hit_list

    # def move(rect, movement, tiles):
    #     collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    #     rect.x += movement[0]
    #     hit_list = Player.collision_test(rect, tiles)
    #     for tile in hit_list:
    #         if movement[0] > 0:
    #             rect.right = tile.left
    #             collision_types['right'] = True
    #         elif movement[0] < 0:
    #             rect.left = tile.right
    #             collision_types['left'] = True
    #     rect.y += movement[1]
    #     hit_list = Player.collision_test(rect, tiles)
    #     for tile in hit_list:
    #         if movement[1] > 0:
    #             rect.bottom = tile.top
    #             collision_types['bottom'] = True
    #         elif movement[1] < 0:
    #             rect.top = tile.bottom
    #             collision_types['top'] = True
    #     return rect, collision_types
    
    def move(self, move_keys, platforms): 
        keys = pygame.key.get_pressed()
        self.update_position(keys, move_keys)
        self.update_image(keys, move_keys)
        self.check_collisions(keys, move_keys, platforms)
        
