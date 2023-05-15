# Rect, Sprites e Colisão

- Aula: Rect, Imagens e Sprites
- Atividade: Encontrar sprites e outros recursos para o game

Para iniciar vamos incluir nosso código base

```python
import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 60

WHITE = (255, 255, 255)

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Animation')

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
```

## 1. Rect

- Rect é um objeto importante para o Pygame
- Rect tem métodos que facilitam a vida de qualquer programador.

- Código abaixo apresenta os métodos com Rect

```bash

```

## 2. Rect e Movimentação

- Dentro o laço principal vamos incluir um `Pygame.Rect` e Desenhalo com `pygame.draw`

```python
rect_x = 0
rect_y = 0

rect1 = pygame.Rect((rect_x, rect_y, 100, 100))
pygame.draw.rect(DISPLAYSURF, RED, rect1)
```

- Assim, temos um retângulo que inicia em `(0,0)` com tamanho de `(100,100)`.

- Para ser possível movimentar o retângulo podemos alterar em tempo de execução as variáveis de `rect_x` e `rect_y`.

- Agora podemos adicionar a movimentação do `Rect` através do teclado.

- Fora do laço principal vamos definir as seguinte variáveis

```python
x = 0
y = 0

rect_x = 0
rect_y = 0
```

```python
for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y = -1
            if event.key == K_DOWN:
                y = 1
            if event.key == K_LEFT:
                x = -1
            if event.key == K_RIGHT:
                x = 1
                
    rect_x += x
    rect_y += y

    rect1 = pygame.Rect((rect_x, rect_y, 100, 100))

    pygame.draw.rect(DISPLAYSURF, RED, rect1)
```

- Porém agora quando soltamos o botão, o `Rect` continua se movimentando.

- Para resolver esse problema, adicionaremos o `listen` para entender quando a tecla foi soltada.

- Adicionamos esse código abaixo do `if` de `KEYDOWN`

```python
if event.type == KEYUP:
            if event.key == K_UP:
                y = 0
            if event.key == K_DOWN:
                y = 0
            if event.key == K_LEFT:
                x = 0
            if event.key == K_RIGHT:
                x = 0
```

### 3. Rect e Colisão

- Vamos adicionar novos `Rects` no nosso jogo, para então verificar quando houve uma colisão.
- Adicione o trecho do `rect` seguinte, é necessário incluir as `constantes` para melhorar a legibilidades.

```python
rect2 = pygame.Rect(
    (
        random.randint(0, DISPLAY_X),
        random.randint(0, DISPLAY_Y),
        RECT_SIZE_X,
        RECT_SIZE_Y
    )
)
```

- Para verificar se houve uma colisão, use `collidepoint`.

```python
if rect1.collidepoint(rect2):
        print("TOCOU")
```

### 4. Imagens e Rect

- Vamos incluir uma imagem, e verificar sua colisão com um outro `rect`.
- Inclua a imagem antes do laço, e também crie um retângulo apartir da imagem.

```python
cat_img = pygame.image.load("class/res/cat.png")

rect1 = cat_img.get_rect()
```

- Para movimentar a imagem vamos usar como referência o `rect`
- Inclua o código após a leitura dos eventos

```python
rect1.x += x
rect1.y += y
```

- Para finalizar vamos pintar todos os elementos na tela.

- O parâmetro `1` no `pygame.draw.rect` indica que somente as bordas serão renderizadas

```python

DISPLAYSURF.blit(cat_img, rect1)

pygame.draw.rect(DISPLAYSURF, RED, rect1, 1)

pygame.draw.rect(DISPLAYSURF, GREEN, rect2)
```

### 5. Sprites

- O Rect pode representar uma forma, mas não um personagem de um jogo
- Já sabemos como incluir uma imagem de um personagem, porém queremos realizar uma animação do mesmo.

- Para isso, devemos chamar uma classe do `pygame` chamada de `Sprites`.

```python

```
