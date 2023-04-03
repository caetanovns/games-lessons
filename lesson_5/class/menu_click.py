import sys
import pygame
from pygame.locals import *
import time
from itertools import cycle

pygame.init()
pygame.display.set_caption('Menu com Pygame')

SCREEN_X = 800
SCREEN_Y = 600

WHITE = (255, 255, 255)
BLUE = "#1562BA"
BLUE_HOVER = "#468EEC"


DISPLAYSURFACE = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

font_large = pygame.font.Font('res/joystix.otf', 48)

font = pygame.font.Font('res/joystix.otf', 24)

clock = pygame.time.Clock()


def draw_text(text, font, color, surface, pos):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = pos
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
    scroll = 800
    while True:
        scroll -= 1

        DISPLAYSURFACE.blit(bg_main_menu, (scroll - 800, 0))
        DISPLAYSURFACE.blit(bg_main_menu, (scroll, 0))

        if scroll <= 0:
            scroll = 800

        # draw_text('main menu', font, (255, 255, 255),
        #           DISPLAYSURFACE, (100, 20))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect((SCREEN_X/3*0) + 60, 500, 150, 50)
        button_2 = pygame.Rect((SCREEN_X/3*1) + 60, 500, 150, 50)
        button_3 = pygame.Rect((SCREEN_X/3*2) + 60, 500, 150, 50)

        pygame.draw.rect(DISPLAYSURFACE, BLUE, button_1, 0, 10)
        pygame.draw.rect(DISPLAYSURFACE, BLUE, button_2, 0, 10)
        pygame.draw.rect(DISPLAYSURFACE, BLUE, button_3, 0, 10)

        click = pygame.mouse.get_pressed()

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(DISPLAYSURFACE, BLUE_HOVER, button_1, 0, 10)
            if click[0]:
                game()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(DISPLAYSURFACE, BLUE_HOVER, button_2, 0, 10)
            if click[0]:
                options()

        draw_text("Night's Adventures", font_large,
                  WHITE, DISPLAYSURFACE, (400, 150))
        draw_text("The Game", font_large, WHITE, DISPLAYSURFACE, (400, 250))

        draw_text('Start', font, WHITE, DISPLAYSURFACE, button_1.center)
        draw_text('Options', font, WHITE, DISPLAYSURFACE, button_2.center)
        draw_text('About', font, WHITE, DISPLAYSURFACE, button_3.center)

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

        draw_text('options', font, (255, 255, 255), DISPLAYSURFACE, (80, 20))

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

        draw_text('Game', font, (0, 0, 0), DISPLAYSURFACE, (60, 20))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)


def credits():
    pass


main_menu()
