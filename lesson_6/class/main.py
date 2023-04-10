import pygame
import sys
from pygame.locals import *
from sprites import *
import datetime

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Animation')

crosshair = Crosshair(DISPLAYSURF)

crosshair_group = pygame.sprite.Group()

crosshair_group.add(crosshair)

rect_colision = pygame.Rect(300, 300, 200, 200)

while True:
    DISPLAYSURF.fill((0, 0, 150))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), rect_colision)

    crosshair_group.draw(DISPLAYSURF)
    crosshair_group.update()

    if (crosshair.another_rect.colliderect(rect_colision)):
        print("PRIMEIRA COLISÃO {}".format(datetime.datetime.now().second))
    
    if (crosshair.rect.colliderect(rect_colision)):
        print("SEGUNDA COLISÃO {}".format(datetime.datetime.now().second))

    pygame.display.update()
    fpsClock.tick(FPS)
