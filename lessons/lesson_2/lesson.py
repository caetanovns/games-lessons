import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 30

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Animation')

# pygame.draw.rect(DISPLAYSURF, RED, (50, 50, 100, 100))

catImg = pygame.image.load('cat.png')
catx = 10
caty = 10

sound = pygame.mixer.Sound("res/game_start.mp3")

pygame.mixer.music.load("res/caves_dawn.mp3")
pygame.mixer.music.play(-1, 0.0)

fontObj = pygame.font.Font('res/candila.otf', 64)

textSurfaceObj = fontObj.render('Aula de Jogos!', True, RED)

textRectObj = textSurfaceObj.get_rect()

textRectObj.center = (200, 150)

bg_main_menu = pygame.transform.scale(
    pygame.image.load('res/bg_image.png'), (800, 600))

while True:
    DISPLAYSURF.blit(bg_main_menu, (0, 0))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                sound.play()

    DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.display.update()
    fpsClock.tick(FPS)
