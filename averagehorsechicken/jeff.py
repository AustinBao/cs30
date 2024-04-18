import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.player = pygame.Rect(-10, 560, 20, 20)
        self.x_vel = 0
        self.y_vel = 0
        self.gravity = 0.7
        self.on_ground = False

    def draw_player(self, offset):
        pygame.draw.rect(display, "blue", self.player.move(offset))

    def controls(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.x_vel = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.x_vel = -5
        else:
            self.x_vel = 0

        if keys_pressed[pygame.K_UP] and self.on_ground:
            self.on_ground = False
            self.y_vel = -15

    def apply_movement(self):
        self.player.centerx += self.x_vel
        self.player.centery += self.y_vel

    def apply_gravity(self):
        self.y_vel = min(self.y_vel + self.gravity, 30)

    def platform_collision(self):
        # Horizontal Collision
        self.player.x += self.x_vel
        collided_platform_index = self.player.collidelist(platforms.platforms)
        if collided_platform_index >= 0:
            collided_platform = platforms.platforms[collided_platform_index]
            if self.x_vel > 0:
                self.player.right = collided_platform.left
                self.x_vel = 0
            elif self.x_vel < 0:
                self.player.left = collided_platform.right
                self.x_vel = 0
        self.player.x -= self.x_vel

        # Vertical Collision
        self.player.y += self.y_vel
        collided_platform_index = self.player.collidelist(platforms.platforms)
        if collided_platform_index >= 0:
            collided_platform = platforms.platforms[collided_platform_index]
            if self.y_vel > 0:
                self.player.bottom = collided_platform.top
                self.y_vel = 0
                self.on_ground = True
            elif self.y_vel < 0:
                self.player.top = collided_platform.bottom
                self.y_vel = 0
        else:
            self.on_ground = False
        self.player.y -= self.y_vel

    def update(self, offset):
        self.controls()
        self.platform_collision()
        self.draw_player(offset)
        self.apply_movement()
        self.apply_gravity()


class Platforms:
    def __init__(self):
        self.platform_data = [
            {"x": -1000, "y": 580, "width": 2000, "height": 100},
            {"x": -1000, "y": -690, "width": 2000, "height": 100},
            {"x": -1000, "y": -690, "width": 100, "height": 2000},
            {"x": -600, "y": 450, "width": 200, "height": 20},
            {"x": -350, "y": 320, "width": 200, "height": 20},
            {"x": -100, "y": 450, "width": 200, "height": 20},
            {"x": 150, "y": 320, "width": 200, "height": 20},
            {"x": 400, "y": 450, "width": 200, "height": 20},
            {"x": -600, "y": 190, "width": 200, "height": 20},
            {"x": -350, "y": 60, "width": 200, "height": 20},
            {"x": -100, "y": 190, "width": 200, "height": 20},
            {"x": 150, "y": 60, "width": 200, "height": 20},
            {"x": 400, "y": 190, "width": 200, "height": 20},
            {"x": -600, "y": -70, "width": 200, "height": 20},
            {"x": -350, "y": -200, "width": 200, "height": 20},
            {"x": -100, "y": -70, "width": 200, "height": 20},
            {"x": 150, "y": -200, "width": 200, "height": 20},
            {"x": 400, "y": -70, "width": 200, "height": 20},
            {"x": -600, "y": -330, "width": 200, "height": 20},
            {"x": -350, "y": -460, "width": 200, "height": 20},
            {"x": -100, "y": -330, "width": 200, "height": 20},
            {"x": 150, "y": -460, "width": 200, "height": 20},
            {"x": 400, "y": -330, "width": 200, "height": 20},
            {"x": 900, "y": -690, "width": 100, "height": 2000},
        ]
        self.platforms = []
        for data in self.platform_data:
            self.platforms.append(pygame.Rect(data["x"], data["y"], data["width"], data["height"]))

    def draw(self, offset):
        for platform in self.platforms:
            pygame.draw.rect(display, "azure4", platform.move(offset))


player = Player()
platforms = Platforms()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill("white")

    offset = pygame.math.Vector2(0, 0)

    # Horizontal Offset
    if player.player.centerx < -1000 + display_width / 2:
        offset.x = 1000
    elif player.player.centerx > 1000 - display_width / 2:
        offset.x = -200
    else:
        offset.x = display_width / 2 - player.player.centerx

    # Vertical Offset
    if player.player.centery < -690 + display_height / 2:
        offset.y = 690
    elif player.player.centery > 680 - display_height / 2:
        offset.y = -80
    else:
        offset.y = display_height / 2 - player.player.centery

    player.update(offset)

    platforms.draw(offset)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()