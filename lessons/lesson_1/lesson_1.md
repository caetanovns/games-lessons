# Games Lessons

Apresentar: Exercício 1.

Assunto: Hello Wolrd com pygames.

## 1. Para iniciar

- Para iniciar, vamos importar a lib do pygames

```bash
import pygame
import sys
from pygame.locals import *
```

## 2. Vamos iniciar o game

- Agora precisamos utilizar o comando de iniciar o game.
- E definimos a surface.

```bash
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
```

## 3. O Game Loop

- O Game loop se reduz a um laço, onde a cada iteração, precisamos atualizar a tela.
- Lembre-se o jogo nada mais é do que trocar imagens, mas de maneira muito rápida.

```bash
while True:
    pygame.display.update()
```

## 4. Capturando eventos

- Agora queremos capturar alguns eventos.
  - Ex.: Fechar o jogo pela própria tela.

```bash
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

## Extras

- Vamos definir algumas configurações extas.

```bash
pygame.display.set_caption('Hello Wolrd')
```

```bash
FPS = 30
fpsClock = pygame.time.Clock()
fpsClock.tick(FPS)
```
