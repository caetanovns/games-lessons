import pygame


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load('res/crosshair.png')
        self.rect = self.image.get_rect()
        self.another_rect = pygame.Rect(0, 0, 20, 20)

    def update(self):
        self.another_rect.center = self.rect.center
        pygame.draw.rect(self.surface, (255, 0, 0), self.another_rect, 1)
        pygame.draw.rect(self.surface, (255, 255, 0), self.rect, 1)

        self.rect.center = pygame.mouse.get_pos()
