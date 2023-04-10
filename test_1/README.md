# Prova AVP1

## Disciplina: Desenvolvimento de Games

### Contexto do jogo

Você é um(a) grande desenvolvedor(a) de games, então recebe a missão de construir um jogo para alerta os perígos que as tartarugas passa, mesmo estando submersas no fundo do mar. Na vida real o que causa ameaça as tartarugas são os lixos que são descartado de maniera inadequada, no entando no nosso jogo serão substituidos por pequenas bombas, que surgem da superfície e caem em uma velocidade e direção constante até o fundo. A tartaruga sempre permanece no fundo do mar, e não tem muitas chances para escapar de todos esses objetos que caem da superfície, ela tem apenas dois movimentos, para **esquerda** e **direita**. Os objetos ficam permanecem caindo durante  todo o tempo que o jogo está em execução, cada bomba que tocar na tartaruga deverá desaparecer, isso significa que houve um dano na tartaruga, no entanto nada mais acontece, então significa que ela pode sofrar diversos danos e ainda contiuna bem.

### Antes de Iniciar

- Utilize este repositório para inicar seu jogo, pois nele já foi incluido as bibliotecas necessárias para a execução do APP.

- Você é livre para criar qualquer diretório ou arquivos que julgar necessário.

- É recomendado que você utilize `FPS = 60` e a tela de `1024x768`, porém é livre para modificar e denifir outro.

### Requisitos da aplicação

- **O Plano de fundo:**
  - Na pasta `res`, tem um arquivo chamado de `background.png`, ele deve ser o plano de fundo do nosso jogo.

  - A imagem deverá ocupar toda a tela do jogo, então lembre-se de manter ela ajustada.

- **A Tartaruga:**
  - Na pasta `res` tem um arquivo chamada de `turtle.png`, este deverá representar o personagem da tartaruga. Lembre de trabalhar como uma sprite sheet.

  - Independente da movimentação a tartaruga sempre deverá executar sua animação, de acordo com o sprite sheet.

  - A tartaruga deverá ficar parte interir da tela, e a única movimentação possível é para a **esquerda** e **direita**

  - A tartaruga tem uma velocidade constante, e você pode decidir qual será, insira uma velocidade que seja compatível com a movimentação da sprite.

  - A sprite sheet deverá acompanhar a movimenação executada pelo usuários, logo se o usuário pressionar o botão esquerdo, tanto o objeto como também a sprite deverá ficar orientada para a esquerda. DICA: utilize a função `pygame.transform.flip()` para inverter a imagem.

- **A Bomba**

  - Temos 2 tipos de bombas que podem surgir dentro do nosso cenário, também se encontram na pasta `res` são elas: `bomb_1.png` e `bomb_2.png`.
  
  - Cada bomba quer surgir no ambiente poderá ser do tipo `bomb_1` ou do tipo `bomb_2`. DICA: Faça um sorteio

  - A bomba poderá ser 3 tamanhos diferentes. Então você pode definir como pequeno, medio ou grande. Ex.: então durante o jogo poderá surgir uma bomba do tipo `bomb_1` com tamanho `1` , como logo após poderá surgir outra do mesmo tipo, agora com tamanho `3`.

  - A bomba também possui uma velocidade diferente. Defina 3 tipos de velocidade, lento, meio, rápido. Portante da mesma forma do tamanho, bombas do mesmo tipo podem cair com velocidade diferentes.

  - Para manter um ambiente desafiador, garanta que sempre surgirão várias bombas ao mesmo tempo.

- **A colisão entre a bomba e a tartaruga**
  - Caso a bomba entre em contato com a tartaruga, a bomba deverá apenas sumir, nada mais precisa ser feito.

  - Em situações que a bomba nunca toca a tartaruga, a sprite da bomba deverá ser deletada, para permitir que novas bombas aparecam no topo da tela. DICA: `[sprite].kill()`

  - Em relação ao sprite temos um problema, pois há espaços não visíveis na imagem. Você deverá ajustar um outro `rect` na imagem, para assim aproximar o `rect` a parte visível da sprite. DICA: Utilize a função `pygame.draw.rect()` para visualizar as bordas das imagens, tanto da tartaruga, quando da bomba.

### Observações gerais

## Envio do Teste

- Para enviar o teste basta apenas compactar (zip) o seu projeto e enviar no portal acadêmico.

Boa Sorte!
