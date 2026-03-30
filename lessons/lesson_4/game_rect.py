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

SPEED = 5
WIDHT = 50

dtX = SPEED
dtY = SPEED

COR = (0,0,0)
BLACK = (0,0,0)

quadrados = []
indexOld = None

rect1 = pygame.Rect(200, 200, 150, 150)

bg_main_menu = pygame.transform.scale(pygame.image.load('bg_main_menu.png'), (SCREEN_X, SCREEN_Y))
pedra = pygame.transform.scale(pygame.image.load('pedra.png'), (150, 150))
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

class Quadrado(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pedra.subsurface((50, 60), (50, 28))
        
        self.image = pygame.transform.scale(self.image, (self.SIZE, self.SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_X)
        self.rect.y = random.randint(0, SCREEN_Y)
    
    def update(self):
        self.image = pygame.transform.scale(self.image, (self.SIZE, self.SIZE))
        pygame.draw.rect(SURFACE, RED, (self.rect.x, self.rect.y, self.SIZE, self.SIZE),1) # QUADRADO
    
    SPEED = 1
    dtX = SPEED
    dtY = SPEED
    SIZE = 60

    cor = sorteio_de_cores()

all_sprites_list = pygame.sprite.Group()

for i in range(1):
    all_sprites_list.add(Quadrado())

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
    
    # SURFACE.fill(WHITE) # BACKGROUND
    SURFACE.blit(bg_main_menu, (scroll - 800, 0))
    SURFACE.blit(bg_main_menu, (scroll, 0))

    if scroll <= 0:
        scroll = 800

    for q in all_sprites_list:
        # VERIFICA SE BATEU NO LADO DIREITO
        if (q.rect.x > SCREEN_X - 50):      
            q.dtX = -SPEED
            
        
        # VERIFICA SE BATEU NO LADO ESQUERDO
        if(q.rect.x < 0):
            q.dtX = SPEED

        # VERIFICAR SE BATEU BAIXO
        if (q.rect.y > SCREEN_Y - 50):
            q.dtY = -SPEED

        # VERIFICA SE BATEU CIMA
        if (q.rect.y < 0):
            q.dtY = SPEED
        # q.cor = sorteio_de_cores() if check_bordas(q) else q.cor

        q.rect.x += q.dtX
        q.rect.y += q.dtY

        # pygame.draw.rect(SURFACE, q.cor, (q.x, q.y, q.width, q.height)) # QUADRADO
        
    #rect1.x += x * SPEED * 5
    #rect1.y += y * SPEED * 5
    pygame.draw.rect(SURFACE, BLACK, rect1)
    # pygame.draw.rect(SURFACE, RED, rect2)
    # indexAtual = all_sprites_list.collidelist(rect1)
    indexAtual = rect1.collidelist(all_sprites_list.sprites())

    if indexAtual != -1 and indexOld != indexAtual:
        print("TOCOU")
        all_sprites_list.sprites()[indexAtual].SIZE /= 2

    if indexOld != indexAtual:
        indexOld = indexAtual

    # SURFACE.blit(pedra, (rect1.x, rect1.y))
    all_sprites_list.update()
    all_sprites_list.draw(SURFACE)
    
    pygame.display.update() # DESENHA NA TELA
    CLOCK.tick(FPS)
