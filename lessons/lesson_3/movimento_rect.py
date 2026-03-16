import pygame
import random

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))


pygame.display.set_caption('Movimento do Retângulo')

dt = 1

width = 50
height = 50
speedX = dt
speedY = dt
x = 0
y = 0

color = (0, 0, 255)

image = pygame.image.load('lessons/lesson_3/dvd.png')
scaled_image = pygame.transform.scale(image, (image.get_width() // 6, image.get_height() // 6))
rect1 = image.get_rect()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def check_boundaries():
    if(x > 800 - 50):
        return True
    
    if (x < 0):
        return True
        
    if (y > 600 - 50):
        return True
        
    if (y < 0):
        return True

    return False

while True:
    fpsClock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dt += 5

            if event.key == pygame.K_DOWN:
                dt -= 5
            

    DISPLAYSURF.fill((0, 0, 0))
    
    if(x > 800 - 50):
        speedX = -dt + random.randint(0, 1)
    
    if (x < 0):
        speedX = dt + random.randint(0, 1)
        
    x += speedX
    
    if (y > 600 - 50):
        speedY = -dt + random.randint(0, 1)
        
    if (y < 0):
        speedY = dt + random.randint(0, 1)
        
    y += speedY
    
    color = random_color() if check_boundaries() else color
    # DISPLAYSURF.blit(scaled_image, (x, y))
    pygame.draw.rect(DISPLAYSURF, color, (x, y, width, height))
    pygame.display.update()
    

    
    