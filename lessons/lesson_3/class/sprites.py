import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SURFACE_COLOR = (167, 255, 100)
COLOR = (255, 100, 98)

fpsClock = pygame.time.Clock()
DISPLAY_X = 800
DISPLAY_Y = 600

DISPLAYSURF = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))

pygame.display.set_caption('Rect e Sprites')

x = 0
y = 0

RECT_SIZE_X = 100
RECT_SIZE_Y = 100

rect_x = 0
rect_y = 0

SPEED = 1

sprite_sheet = pygame.image.load('class/res/sprites.png')


class Person(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []

        for i in range(4):
            sprite_row = []
            for j in range(8):
                img = sprite_sheet.subsurface(
                    (j * 64, 512 + (i * 64)), (64, 64))
                sprite_row.append(img)
            self.sprites.append(sprite_row)

        self.index = 0
        self.direction = 2
        self.animation = False

        self.image = self.sprites[self.direction][self.index]
        self.image = pygame.transform.scale(self.image, (64*5, 64*5))
        self.rect = self.image.get_rect()

    def update(self):
        if self.animation == True:
            self.index += 0.25
            if self.index >= 8:
                self.index = 0
        self.image = self.sprites[self.direction][int(self.index)]
        self.image = pygame.transform.scale(self.image, (64*1.5, 64*1.5))
        


rect2 = pygame.Rect(
    (
        random.randint(0, DISPLAY_X),
        random.randint(0, DISPLAY_Y),
        RECT_SIZE_X,
        RECT_SIZE_Y
    )
)

cat_img = pygame.image.load("class/res/cat.png")

rect1 = cat_img.get_rect()

person = Person()
person.rect.x = 100
person.rect.y = 100

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(person)

direction = [0,0]

while True:

    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            person.animation = True
            if event.key == K_UP:
                person.direction = 0
                direction[1] = -1
                y = SPEED * -1
            if event.key == K_DOWN:
                person.direction = 2
                direction[1] = 1
                y = SPEED * 1
            if event.key == K_LEFT:
                person.direction = 1
                x = SPEED * -1
                direction[0] += -1
            if event.key == K_RIGHT:
                person.direction = 3
                direction[0] += 1
                x = SPEED * 1

        if event.type == KEYUP:
            #person.animation = False
            #person.index = 0
            if event.key == K_UP:
                y = 0
                direction[1] = 0
            if event.key == K_DOWN:
                y = 0
                direction[1] = 0
            if event.key == K_LEFT:
                x = 0
                direction[0] = 0
            if event.key == K_RIGHT:
                x = 0
                direction[0] = 0
    
    keys = pygame.key.get_pressed()
    
    if not (keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]):
        person.animation = False
        person.index = 0
        
    # rect1.x += x
    # rect1.y += y
    #person.rect.x += x
    #person.rect.y += y
    # print(direction)
    person.rect.move_ip(direction[0], direction[1])
    
    # rect1.move_ip(0, 1)
    DISPLAYSURF.blit(cat_img, rect1)

    pygame.draw.rect(DISPLAYSURF, RED, rect1, 1)

    pygame.draw.rect(DISPLAYSURF, GREEN, rect2)

    all_sprites_list.update()
    all_sprites_list.draw(DISPLAYSURF)
    pygame.display.update()

    fpsClock.tick(FPS)
