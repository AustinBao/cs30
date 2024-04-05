import pygame


class Player(pygame.sprite.Sprite):

	# static variables to control jump
	jumping = False
	Y_GRAVITY = 0.6
	JUMP_HEIGHT = 13
	Y_VELOCITY = JUMP_HEIGHT


	def __init__(self, x, y, scale, img):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(f'imgs/characters/{img}')
		self.x = x
		self.y = y
		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)


	def move(self):
	
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and keys[pygame.K_d]:
			self.y -= 5
			self.x += 5
		elif keys[pygame.K_w] and keys[pygame.K_a]:
			self.y -= 5
			self.x -= 5
		elif keys[pygame.K_s] and keys[pygame.K_d]:
			self.y += 5
			self.x += 5
		elif keys[pygame.K_s] and keys[pygame.K_a]:
			self.y += 5
			self.x -= 5
		elif keys[pygame.K_a]:
			self.x -= 5
		elif keys[pygame.K_d]:
			self.x += 5
		elif keys[pygame.K_w]:
			self.y -= 5
		elif keys[pygame.K_s]:
			self.y += 5
		elif keys[pygame.K_SPACE]:
			Player.jumping = True

		
		if Player.jumping:
			self.y -= Player.Y_VELOCITY
			Player.Y_VELOCITY -= Player.Y_GRAVITY
			if Player.Y_VELOCITY < -Player.JUMP_HEIGHT:
				Player.jumping = False
				Player.Y_VELOCITY = Player.JUMP_HEIGHT