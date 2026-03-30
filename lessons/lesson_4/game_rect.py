import pygame
import random
FPS = 120
CLOCK = pygame.time.Clock()
pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

SCREEN_X = 800
SCREEN_Y = 600

SURFACE = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.RESIZABLE)
pygame.display.set_caption("Primeiro Jogo")

x = 0
y = 0

SPEED = 1
WIDHT = 50

dtX = SPEED
dtY = SPEED

COR = (0,0,0)
BLACK = (0,0,0)

quadrados = []
indexOld = None

rect1 = pygame.Rect(100, 100, WIDHT, WIDHT)

bg_main_menu = pygame.transform.scale(pygame.image.load('bg_main_menu.png'), (SCREEN_X, SCREEN_Y))
scroll = 800

def random_pos():
    return (random.randint(0,SCREEN_X),random.randint(0,SCREEN_Y))

def sorteio_de_cores():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def check_bordas(q):
    if (q.x > SCREEN_X - 50):      
        return True
    if(q.x < 0):
        return True
    if (q.y > SCREEN_Y - 50):
        return True
    if (q.y < 0):
        return True
    
    return False

class Quadrado(pygame.Rect):

    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)

    SPEED = 5
    dtX = SPEED
    dtY = SPEED

    cor = sorteio_de_cores()

for i in range(1):
    quadrados.append(Quadrado(random.randint(0, SCREEN_X - 50), random.randint(0, SCREEN_Y - 50)))

while True:
    SCREEN_X, SCREEN_Y = pygame.display.get_surface().get_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = -1
            if event.key == pygame.K_DOWN:
                y = 1
            if event.key == pygame.K_LEFT:
                x = -1
            if event.key == pygame.K_RIGHT:
                x = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y = 0
            if event.key == pygame.K_DOWN:
                y = 0
            if event.key == pygame.K_LEFT:
                x = 0
            if event.key == pygame.K_RIGHT:
                x = 0
    scroll -= 1
    # print(rect_cat.colliderect(rect2))
    
    SURFACE.fill(WHITE) # BACKGROUND
    SURFACE.blit(bg_main_menu, (scroll - 800, 0))
    SURFACE.blit(bg_main_menu, (scroll, 0))

    if scroll <= 0:
        scroll = 800
            
    for q in quadrados:
        # VERIFICA SE BATEU NO LADO DIREITO
        if (q.x > SCREEN_X - 50):      
            q.dtX = -SPEED + random.randint(-2,2)
        
        # VERIFICA SE BATEU NO LADO ESQUERDO
        if(q.x < 0):
            q.dtX = SPEED + random.randint(-2,2)

        # VERIFICAR SE BATEU BAIXO
        if (q.y > SCREEN_Y - 50):
            q.dtY = -SPEED + random.randint(-2,2)

        # VERIFICA SE BATEU CIMA
        if (q.y < 0):
            q.dtY = SPEED + random.randint(-2,2)

        # q.cor = sorteio_de_cores() if check_bordas(q) else q.cor

        q.x += q.dtX
        q.y += q.dtY

        pygame.draw.rect(SURFACE, q.cor, (q.x, q.y, q.width, q.height)) # QUADRADO
        
    rect1.x += x * SPEED * 5
    rect1.y += y * SPEED * 5
    pygame.draw.rect(SURFACE, BLACK, rect1)
    # pygame.draw.rect(SURFACE, RED, rect2)
    
    # rect_cat.topleft = (quadrados[0].x, quadrados[0].y)
    # SURFACE.blit(cat_image, rect_cat)
    indexAtual = rect1.collidelist(quadrados)

    if indexAtual != -1 and indexOld != indexAtual:
        quadrados[indexAtual].cor = sorteio_de_cores()

    if indexOld != indexAtual:
        indexOld = indexAtual

    pygame.display.update() # DESENHA NA TELA
    CLOCK.tick(FPS)
