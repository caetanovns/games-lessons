import pygame
import sys
import random
from pygame.locals import *
from sprites import *


pygame.init()

FPS = 60

WHITE = (0, 0, 0)
DISPLAY_X = 1024
DISPLAY_Y = 768

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y), pygame.RESIZABLE)

pygame.display.set_caption('Animation')

background = pygame.image.load('res/bg_blue.png')
pygame.mouse.set_visible(False)


crosshair = Crosshair()
background = Background(DISPLAY_X, DISPLAY_Y)


crosshair_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
target_group = pygame.sprite.Group()

crosshair_group.add(crosshair)
background_group.add(background)

for i in range(20):
    target = Target(random.randrange(0, DISPLAY_X), random.randrange(0, DISPLAY_Y))
    target_group.add(target)


while True:

    background_group.draw(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            crosshair.fire()
            pygame.sprite.spritecollide(crosshair, target_group, True)
        if event.type == KEYDOWN:
            if event.key == K_r:
                crosshair.reload()

    target_group.draw(DISPLAYSURF)
    crosshair_group.draw(DISPLAYSURF)

    target_group.update()
    crosshair_group.update()
    background_group.update()
    pygame.display.update()
    fpsClock.tick(FPS)
