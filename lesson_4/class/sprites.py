import pygame
import math


class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('res/target.png')
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/crosshair.png')
        self.rect = self.image.get_rect()

        self.shot_gun = pygame.mixer.Sound('res/shotgun.mp3')
        self.shot_gun_reload = pygame.mixer.Sound('res/reload.mp3')

        # pygame.draw.rect(self.image, (0, 0, 0), self.rect, 1)

    def fire(self):
        self.shot_gun.play()

    def reload(self):
        self.shot_gun_reload.play()

    def update(self):

        self.rect.center = pygame.mouse.get_pos()
        self.rect.center = (self.rect.x + 40, self.rect.y + 40)


class Background(pygame.sprite.Sprite):
    def __init__(self, display_x, display_y):
        super().__init__()
        self.d_x = display_x
        self.d_y = display_y
        self.image = pygame.surface.Surface([display_x, display_y])
        self.bg = pygame.image.load('res/bg_blue.png')
        self.rect = self.bg.get_rect()

    def update(self):
        tiles = math.ceil(self.d_x / self.bg.get_width())

        width = self.bg.get_width()
        height = self.bg.get_height()

        for i in range(tiles):
            for j in range(tiles):
                self.image.blit(self.bg, (j * width, i * height))
