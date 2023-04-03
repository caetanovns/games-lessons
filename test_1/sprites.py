import pygame
import random


class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
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
        

    def update(self):
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


class Bomb(pygame.sprite.Sprite):

    def __init__(self, pos_x):
        super().__init__()

        self.image = pygame.image.load(
            'res/bomb_{}.png'.format(random.randint(1, 2)))
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.speed = random.choices([2, 4, 7], k=1)[0]
        self.rect.x = pos_x

    def update(self):
        self.rect.y += self.speed

        if (self.rect.y > 768):
            self.kill()
