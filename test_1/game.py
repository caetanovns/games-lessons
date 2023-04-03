import pygame
import sys
import random
from pygame.locals import *
from sprites import *

pygame.init()

FPS = 60

WHITE = (255, 255, 255)

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1024, 768))

pygame.display.set_caption('Animation')

background = pygame.image.load('res/background.png')

background = pygame.transform.scale(background, (1024, 768))

turtle = Turtle()

turtle_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

turtle_group.add(turtle)

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    bomb_group.draw(DISPLAYSURF)
    bomb_group.update()

    turtle_group.draw(DISPLAYSURF)
    turtle_group.update()
    
    pygame.sprite.spritecollide(turtle, bomb_group, True)
        

    if len(bomb_group) < 10:
        bomb_group.add(Bomb(random.randint(0, 1024)))
    pygame.display.update()
    fpsClock.tick(FPS)
