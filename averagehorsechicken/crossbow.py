import pygame


class Crossbow:
    def __init__(self, pos):
        self.image = pygame.image.load("imgs/items/0.png")
        self.scaled_img = pygame.transform.scale(self.image, (25, 50))
        self.rect = self.scaled_img.get_rect(center=pos)
        self.shoot_timer = 0
        self.projectiles = pygame.sprite.Group()

    def shoot(self):
        projectile = Projectile((self.rect.centerx + 12, self.rect.top))  # Shoot from the top of the crossbow
        self.projectiles.add(projectile)

    def update(self):
        self.projectiles.update()
        self.shoot_timer += 1
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
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()



