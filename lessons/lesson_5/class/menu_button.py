import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Menu com Pygame')

SCREEN_X = 800
SCREEN_Y = 600

DISPLAYSURFACE = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

font = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()


def quit_game():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


bg_main_menu = pygame.transform.scale(
    pygame.image.load('res/bg_main_menu.png'), (SCREEN_X, SCREEN_Y))

bg_options = pygame.transform.scale(
    pygame.image.load('res/bg_options.png'), (SCREEN_X, SCREEN_Y))

bg_credit = pygame.transform.scale(
    pygame.image.load('res/bg_credits.png'), (SCREEN_X, SCREEN_Y))

bg_game = pygame.transform.scale(
    pygame.image.load('res/bg_game.png'), (SCREEN_X, SCREEN_Y))


def main_menu():
    while True:
        DISPLAYSURFACE.blit(bg_main_menu, (0, 0))

        draw_text('main menu', font, (255, 255, 255), DISPLAYSURFACE, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect((SCREEN_X/3*0) + 60, 500, 150, 50)
        button_2 = pygame.Rect((SCREEN_X/3*1) + 60, 500, 150, 50)
        button_3 = pygame.Rect((SCREEN_X/3*2) + 60, 500, 150, 50)

        click = pygame.mouse.get_pressed()

        if button_1.collidepoint((mx, my)):
            if click[0]:
                game()
        if button_2.collidepoint((mx, my)):
            if click[0]:
                options()

        pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), button_1)
        pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), button_2)
        pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), button_3)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def options():
    running = True
    while running:
        DISPLAYSURFACE.blit(bg_options, (0, 0))

        draw_text('options', font, (255, 255, 255), DISPLAYSURFACE, 20, 20)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)


def game():
    running = True
    while running:
        DISPLAYSURFACE.blit(bg_game, (0, 0))

        draw_text('game', font, (255, 255, 255), DISPLAYSURFACE, 20, 20)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)


def credits():
    pass


main_menu()
