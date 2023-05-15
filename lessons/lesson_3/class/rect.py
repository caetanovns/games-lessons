import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

SPEED = 5
rect2 = pygame.Rect(
    (
        random.randint(0, DISPLAY_X),
        random.randint(0, DISPLAY_Y),
        RECT_SIZE_X,
        RECT_SIZE_Y
    )
)

while True:

    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y = SPEED * -1
            if event.key == K_DOWN:
                y = SPEED * 1
            if event.key == K_LEFT:
                x = SPEED * -1
            if event.key == K_RIGHT:
                x = SPEED * 1

        if event.type == KEYUP:
            if event.key == K_UP:
                y = 0
            if event.key == K_DOWN:
                y = 0
            if event.key == K_LEFT:
                x = 0
            if event.key == K_RIGHT:
                x = 0

    rect_x += x
    rect_y += y

    rect1 = pygame.Rect((rect_x, rect_y, RECT_SIZE_X, RECT_SIZE_Y))

    pygame.draw.rect(DISPLAYSURF, RED, rect1)

    pygame.draw.rect(DISPLAYSURF, GREEN, rect2)

    pygame.display.update()

    fpsClock.tick(FPS)
