import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Hello Wolrd')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)