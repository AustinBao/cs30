import pygame


class Crossbow:
    def __init__(self, pos):
        self.image = pygame.image.load("imgs/items/0.png")
        # scale to fit the grid which goes up by 25 increments
        self.scaled_img = pygame.transform.scale(self.image, (25, 50))
        self.rect = self.scaled_img.get_rect(center=pos)
        self.shoot_timer = 0
        self.projectiles = pygame.sprite.Group()

    def shoot(self):
        # Shoot from the top of the crossbow; add 12 to center the arrow to the center of the image
        projectile = Projectile((self.rect.centerx + 12, self.rect.top))
        # adds to the sprite.Group(), a container which holds a bunch of sprites (specifically, they are "Projectile" sprites)
        self.projectiles.add(projectile)

    def update(self):
        # updates the arrows position
        self.projectiles.update()
        self.shoot_timer += 1
        # shoots an arrow every 60 frames. Since my game runs in 60 fps, it shoots one arrow every one second that passes
        if self.shoot_timer >= 60:
            self.shoot_timer = 0
            self.shoot()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/projectiles/arrow.png")
        self.rect = self.image.get_rect(center=pos)
        self.speed = -5

    def update(self):
        # moves the arrow across the screen by a speed of 5
        self.rect.y += self.speed
        # arrow projectile is removed/killed when it leaves the top of the screen (y < 0)
        if self.rect.bottom < 0:
            self.kill()
