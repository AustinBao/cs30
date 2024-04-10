import pygame


class Player(pygame.sprite.Sprite):

	# static variables to control jump
	jumping = False
	Y_GRAVITY = 0.6
	JUMP_HEIGHT = 13
	Y_VELOCITY = JUMP_HEIGHT


	def __init__(self, x, y, scale, img):
		pygame.sprite.Sprite.__init__(self)
		self.original_img = pygame.image.load(f'imgs/characters/{img}')
		self.jumping_img = pygame.image.load(f'imgs/characters/jumping.png')
		self.scale = scale
		self.x = x
		self.y = y
		self.image = pygame.transform.scale(self.original_img, (int(self.original_img.get_width() * scale), int(self.original_img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)


	def move(self):
	
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and keys[pygame.K_d]:
			Player.jumping = True
			self.x += 5
		elif keys[pygame.K_SPACE] and keys[pygame.K_a]:
			Player.jumping = True
			self.x -= 5
		elif keys[pygame.K_a]:
			self.image = pygame.transform.flip(self.original_img, True, False)
			self.image = pygame.transform.scale(self.image, (int(self.original_img.get_width() * self.scale), int(self.original_img.get_height() * self.scale)))
			self.x -= 5
		elif keys[pygame.K_d]:
			self.image = pygame.transform.flip(self.original_img, False, False)
			self.image = pygame.transform.scale(self.image, (int(self.original_img.get_width() * self.scale), int(self.original_img.get_height() * self.scale)))
			self.x += 5
		elif keys[pygame.K_w]:
			self.y -= 5
		elif keys[pygame.K_s]:
			self.y += 5
		elif keys[pygame.K_SPACE]:
			Player.jumping = True

		
		if Player.jumping:
			if keys[pygame.K_a]:
				self.image = pygame.transform.flip(self.jumping_img, True, False)
				self.image = pygame.transform.scale(self.image, (int(self.jumping_img.get_width() * self.scale), int(self.jumping_img.get_height() * self.scale)))
			else:
				self.image = pygame.transform.scale(self.jumping_img, (int(self.jumping_img.get_width() * self.scale), int(self.jumping_img.get_height() * self.scale)))
			self.y -= Player.Y_VELOCITY
			Player.Y_VELOCITY -= Player.Y_GRAVITY
			
			if Player.Y_VELOCITY < -Player.JUMP_HEIGHT:
				Player.jumping = False
				self.image = pygame.transform.scale(self.original_img, (int(self.original_img.get_width() * self.scale), int(self.original_img.get_height() * self.scale)))
				Player.Y_VELOCITY = Player.JUMP_HEIGHT

