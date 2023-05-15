# Introdução ao Unity

## Vamos adicionar a movimentaçao do piso
- Esta movimentação faz parte do jogo, para tornar algo mais dinâmico
- Vamos executar a mesma estratégia adotada pelo pygame
- Inclua o script ground.cs abaixo dentro do objeto piso
    ```````cs
    [SerializeField]
        private float speed = 0.01f;

        private Vector3 initialPosition;

        private float imagesize;

        private void Awake()
        {
            this.initialPosition = this.transform.position;
            this.imagesize = this.GetComponent<SpriteRenderer>().size.x;
        }

        // Update is called once per frame
        void Update()
        {
            this.transform.Translate(Vector2.left * this.speed * Time.deltaTime);
            
            if (this.initialPosition.x - this.transform.position.x > this.imagesize)
            {
                this.transform.position = this.initialPosition;
            }
        }
    ````````
- Para finalizar, precisamos duplicar o piso e coloca-lo lado a lado, da mesma forma do pygame.

- Teste e execute para ver o resultado.

## Alterando a posição do cano
- Queremos fazer com que os canos sejam alterados dinamicamente sua posição
- Para isso, podemos alterar a posição do Y de cada cano quando for gerado
- Então vamos fazer uma translação do objeto

    ```````cs
    private void Awake()
    {
        this.transform.Translate(Vector3.up * Random.Range(-1.5f,1.5f));
    }
    ````````
- Ou seja, faremos um sorteio de um valor que ele será transladado.

## Anulando forças do pássaro

- Vamos anular a velocidade do pássaro, quando o jogador clica no botão.
 
    ```````cs
    if (Input.GetButtonDown("Fire1"))
            {
                this.fisica.velocity = Vector2.zero;
                this.fisica.AddForce(Vector2.up * this.force, ForceMode2D.Impulse);
            }
    ````````

## Destruindo obstáculos

- Se notarmos na cena em execução, os canos continuam sendo criados e indo ao infinito;
- Isso não é bacana, pois oculpa espaço em memória e recursos do console;

- A nossa estratégia é incluir um objeto fora da cena, para fazer que quando o cano toque no objecto ele faça uma autodestruição.

- Para isso faça o seguinte:
 - Na cena, faça:
    - Crie um GameObject Vazio
      - Vamo adicionar um Box Collider 2D, pois precisamos de identifiar a colisão.
      - Vamos marcar como um gatilho, faça que isso seja notificado para o objeto.
    - No nosso prefab do cano, precisamos:
      - Adicione o componente RigidBody2D;
      - Vamos Executar o jogo e notar o comportamento;
      - Queremos anular esse moviemntos físicos do Cano;
      - Para isso, marque o ``BodyType`` como ``Kinematic``
    - No script do cano, faça:
      - Ou seja, quando o Cano tocar no Box Collider ele seja destruido.
    ``````cs
    private void OnTriggerEnter2D(Collider2D collider)
        {
            this.destroy();
        }

        public void destroy()
        {
            GameObject.Destroy(this.gameObject);
        }
    ``````
## Tela de GameOver
- Inclua a imagem do ``Game Over`` dentro dos ``assets``
- Agora na ``Hierarquia`` crie um ``UI > Image``
- Note que ele criar um objeto ``Canvas`` e dentro dele nossa ``image``. Sempre que criamos uma UI a unity inclui dentro de um canvas.
- Agora na imagem, inclua no ``Source Image`` a imagem do game over.
- Centralize no meio da tela
- Note que ela fica meio achatada, para isso: Clique no botão de ``Set Native Size``.
- No entanto se executarmos o jogo notamos que ele sempre aparece no meio da tela, queremos que seja exibida quando o usuário tocar em algum cano.
- Então no objeto ``inspetor`` desmaque a caixa de exibição.
- Nossa estratégia será de exibir ou não a nossa image.

### Script Game Over

- Vamos definir um ``GameObject`` chamado de ``Diretor`` e também crie um script com o mesmo nome.
- Ele será o responsável por colocar a nossa image de ``Game Over``.
- O Time faz com que o tempo pare do nosso jogo
- Faça o seguinte script:
    
    ```````cs
        [SerializeField]
        private GameObject imagem;

        public void FinalizarJogo()
        {
            Time.timeScale = 0;
            this.imagem.SetActive(true);
        }
    ````````
- Esse script ja faz com que o jogo seja finalizado, no entanto para finalizar precisamos de identificar quando o pássaro tocar em alguma ``cano`` ou no ``chão``.
- Complemeente o script do pássro.

    ```````cs
    private Diretor diretor;

    private void Awake()
    {
        this.diretor = GameObject.FindObjectOfType<Diretor>();
    }

    private void OnCollisionEnter2D(Collision2D collision)
        {
            this.fisica.simulated = false;
            this.diretor.FinalizarJogo();
        }
    ````````

## Vamos Reiniciar o Jogo
- Agora precisamos reiniar um nosso jogo.
- Dentro do ``Canvas`` inclua um ``Panel``, faça com que a ``image`` seja filha do ``panel``.
- O nosso script ``Diretor`` seja o responsável por ``finalizar/reiniciar`` o jogo.
- O script completo ficará assim:
    ```````cs
    public class directorscene : MonoBehaviour
    {
        [SerializeField]
        private GameObject imagem;

        private bird passaro;

        private void Start()
        {
            this.passaro = GameObject.FindObjectOfType<bird>();
        }

        public void RestartGame()
        {
            this.imagem.SetActive(false);
            Time.timeScale = 1;
            this.passaro.Restart();

            pipe[] pipes = GameObject.FindObjectsOfType<pipe>();
            foreach(pipe p in pipes)
            {
                p.destroy();
            }
        }
    }
    ````````
- Agora só precisamos ir no pássaro e implementar o método de ``Restart()``;
- Vamos guardar a posição inicial do pássaro, quando for reiniciado, vamos basicamente trocar sua posição atual pela posição inicial.
    `````````cs
    private Vector3 initialPosition;

    private void Awake()
    {
        this.initialPosition = this.transform.position;
        this.fisica = this.GetComponent<Rigidbody2D>();
        this.diretor = GameObject.FindObjectOfType<directorscene>();
    }

    public void Restart()
    {
        this.transform.position = this.initialPosition;
        this.fisica.simulated = true;
    }
    ``````````
