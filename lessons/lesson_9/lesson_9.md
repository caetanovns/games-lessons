# Inserindo os texts e a pontuação


## Vamos exibir um texto dentro do nosso jogo

- Para inserir o texto no jogo, vá no ``canvas`` e adicione um ``Legacy Text``
- Coloque a cor em amerelo
- Posicione corretamente o texto
- Adicone a fonte

## Vamos contar os pontos
- Serão contados pontos a cada vez que o pássaro passar pelo obstáculos

- Crie um GameObject na tela, chamado de ``Pontos``, então crie um script para ele.

- Precisamos de um script para pontuação, então adicione um arquivo chamado de ``Score``
``````cs
public class Score : MonoBehaviour
{
    private int pontos;

    [SerializeField]
    private Text texto;

    public void adicionar()
    {
        this.pontos++;
        this.texto.text = this.pontos.ToString();
    }

    public void reiniciar()
    {
        this.pontos = 0;
        this.texto.text = this.pontos.ToString();
    }
}
``````

- Vamos contar os pontos quando os obstáculso passam pelo ``pipe``

```````cs
private Score score;

private void Start()
{
    this.score = GameObject.FindObjectOfType<Score>();
}

void Update()
{
    if (!this.point && this.transform.position.x < this.positionBird.x)
    {
        this.point = true;
        this.score.adicionar();
    }
}
```````


## Zerar pontuação
- Se notar, os pontos estão acumulando mesmo reiniando o jogo.
- Vamos precisar zerar essa pontuação.

- Vamos adicioanr o método reiniar no script do ``Score``

``````cs
public void reiniciar()
{
    this.pontos = 0;
    this.texto.text = this.pontos.ToString();
}
``````

- Então agora no editor da cena, podemos chamar essa referêcia e reinicia-lo.

## Adicione o Som

- Para adionar uma trilha, cire um ``GameObject`` do Tipo ``AudioSource``
- Adicione o Som de Trilha dentro do componente
- Deixe em Loop e que seja executado quando o jogo carregar.
- No ``GameObject`` do ``Pontos``, adicione um componente chamado de ``AudioSource``
- No parâmetro de ``AudioClip``, adicione o som da pontuação.

- No script do ``Score``, vamos adicionar o componente de audio.

```````cs
private AudioSource audio;

public void Awake()
{
    this.audio = this.GetComponent<AudioSource>();
}
```````

# Exercício 

- Adicone o som de quando o jogador faz o pássaro pular e quando o pássaro tocar em algo.