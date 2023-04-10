import pygame
import random


class Turtle(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        turtle_sheet = pygame.image.load('res/turtle.png')
        self.sprites = []
        for i in range(4):
            image = turtle_sheet.subsurface((i*48, 0), (48, 48))
            self.sprites.append(image)

        self.index = 0
        self.direction = 1

        self.image = self.sprites[self.index]

        self.image = pygame.transform.scale(self.image, (48*3, 48*3))
        self.rect = self.image.get_rect()
        self.rect.center = (512, 500)
        self.collision_rect = pygame.Rect(0, 0, 60, 30)
        self.collision_rect.center = self.rect.center

    def update(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.collision_rect, 1)
        pygame.draw.rect(self.surface, (255, 0, 0), self.rect, 1)
        self.collision_rect.center = self.rect.center
        self.index += 0.08
        if self.index >= 4:
            self.index = 0
        self.image = self.sprites[int(self.index)]

        if self.direction:
            self.image = pygame.transform.scale(self.image, (48*3, 48*3))
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (48*3, 48*3))

        self.handle_keys()

    def handle_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.direction = 0

        if key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.direction = 1

    def collides_with(self, other_rect):
        return self.collision_rect.colliderect(other_rect)


class Bomb(pygame.sprite.Sprite):

    def __init__(self, pos_x, surface):
        super().__init__()
        self.surface = surface

        self.speed = random.choices([1, 2, 4], k=1)[0]

        self.size = random.choices([1, 2, 4], k=1)[0]

        self.image = pygame.image.load(
            'res/bomb_{}.png'.format(random.randint(1, 2)))

        self.image = pygame.transform.scale(
            self.image, (24 * self.size, 24 * self.size))
        self.rect = self.image.get_rect()

        self.collision_rect = pygame.Rect(0, 0, 15 * self.size, 15 * self.size)
        self.collision_rect.center = self.rect.center

        self.rect.x = pos_x

    def update(self):

        self.rect.y += self.speed
        self.collision_rect.center = self.rect.center
        pygame.draw.rect(self.surface, (0, 0, 0), self.collision_rect, 1)
        if (self.rect.y > 768):
            self.kill()
