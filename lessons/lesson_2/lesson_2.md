# Games Lessons

Apresentar: TDE 1, Exercício 1 e 2.

Este repositório será utilizado para armazenar as aulas de Jogos.

Assunto: Cores, Imagens, Rect

## 1. Para iniciar

Vamos incluir o bloco básico que precisamos para iniciar nossa jogo com o Pygame.

```bash
import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Animation')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
```

## 2. Cores

```bash
pygame.Color(255, 0, 0)

pygame.draw.rect(DISPLAYSURF, RED, (50, 50, 100, 100))
```

## 3. Imagens

- Com o `pygame.image.load`, podemos carregar imagens e gif dentro do nosso game.

```bash
catImg = pygame.image.load('cat.png')
catx = X
caty = Y
```

- Podemos alterar as variáveis de X e Y da imagem para assim movimentar.
- Dentro do Laço do jogo, podemos fazer alguma movimentação com o personagem.

```bash
catx+=1
```

## 4. Som

- Podemos executar sons com o Pygame
- Temos abaixo um exemplo de execução de som de **efeito**

```bash
sound = pygame.mixer.Sound("filename.ext")
sound.play()
sound.stop()
```

- Podemos também executar sons em modo de **background**
- No método `play(-1, 0.0)`, o valor `-1` indica que a música será reproduzida infinitamente. O Valor `0.0`, indica o instante que a música iniciará

```bash
pygame.mixer.music.load("filename.ext")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()
```

- Vamos fazer com que o som seja executado quando uma tecla seja pressionada.
- Dentro do laço que faz a leitura dos eventos, podemos incluir este trecho
- Sempre temos que entender o tipo de evento, para depois então identificar a tecla pressionada

```bash
if event.type == KEYDOWN:
    if event.key == K_SPACE:
        sound.play()
```

## 5. Fonts

- Assim podemos colocar as fontes

```bash
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
```

- Dentro do laço principal do game, render o texto mostrar o texto, para isso utilizamos a função `blit()`.

```bash
DISPLAYSURF.blit(textSurfaceObj, textRectObj)
```
