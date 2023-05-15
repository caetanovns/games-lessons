import pygame
import sys
from pygame.locals import *

pygame.init()

fps = 60

fps_clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Nosso primeiro jogo")

RED = pygame.Color(255, 0, 0)

catImg = pygame.image.load("res/cat.png")
catX = 800
catY = 100

sound = pygame.mixer.Sound("res/game_start.mp3")
# sound.play()

# pygame.mixer.music.load("res/caves_dawn.mp3")
# pygame.mixer.music.play(-1, 0.0)

font_obj = pygame.font.Font('res/candila.otf', 64)

text = font_obj.render("Menu do Game", True, RED)

while True:
    display_surface.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                sound.play()

    display_surface.blit(catImg, (catX, catY))
    display_surface.blit(text, (100, 100))
    pygame.display.update()
    fps_clock.tick(fps)
    if catX >= 0:
        catX -= 5
