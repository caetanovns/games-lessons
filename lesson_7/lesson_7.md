# Introdução ao Unity


## Vamos recriar um jogo famoso, o flappy bird

- Inicie adicionando os elementos visuais do jogo
    - As imagens de background, da base e do personagem

- Execute para visualizar a cena. Lembre-se de manter tudo dentro da cena para que possa ser visualizado.

### **Rigidbody 2d**

- Podemos adicionar componentes no nosso objeto
- Por padrão todo objeto tem apena o componente de ``transform```. Este que contem apenas as coordenadas do objeto.

- Para adicionar clique em ``Add Component`` e pesquise por ``Rigidbody 2D``.

- Aplicado isso, vamos executar e ver o que deve aconter. Vemos que ele deve cair....

- Queremos que ele não ultrapasse a nossa base, para isso precisamos adicionar um componente na nossa base.

- Adicione a base o componente Collider, nesse caso um ``Box Collider 2D``.

- **O que acontece agora se executarmos novamente o jogo?**

- Personagem continua caindo, porque ?

- O Mesmo também precisar de um collider. Então vamos fazer o mesmo processo para o personagem. Adicione para um Circle Collider 2D.

- Vamos ver o resultado.

- É possível notar que tem uma certa distância do solo, isso acontece porque o collider tem uma pequena diferença em relação ao sprite do personagem.

- Para corrigir esse pequeno problema, podemos adicionar um ``Polygon Collider 2D``. Nele podemos fazer um mapeamento mais específico do personagem.

- Vamos experimentar novamente.

## Adicionar os canos no cenário

- Precisamos adicionar um cano que vem da base do cenário e outro de cima.

- Para isso, basta apenas adicionar 2 objetos com a imagem do cano.

- Para melhorar nosso código, podemos agrupar. Para isso faça: Selecione os dois elemtentos, e com o botão direito faça ``create empty parent``. Assim teremos dois elemtos que podemos manipular com um único objeto.

- Lembre-se de adicionar os ``Box Collider 2D`` em cada cano.

## Adicionando os scripts ao Cano

- Com a unity, pode criar scripts (programação) assim podemos executar ações específicas do nosso jogo.

- Em todo scripts, teremos o metodo update. ele é o resposável pela execução do script no nosso game loop.

- crie um script chamado de ``pipe``, ele será resposável pela movimentação dos canos.

- Abra o script dentro de um editor de texto e faça a seguinte alteração

``````cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pipe : MonoBehaviour
{
    
    // Update is called once per frame
    void Update()
    {
        this.transform.Translate(Vector3.left);
    }
}
``````

- Vamo executar o jogo e ver o resultado.

- O que aconteceu aqui? O cano passar super rápido.

- Para isso, pdemos alterar nosso script. e incluir um força de movimentação menor. Para isso faça.

```````cs
this.transform.Translate(Vector3.left * 0.01f);
```````

## Adicionando script ao personagem

- Precisamos fazer que ao botão de clique o personagem seja impulsionado para cima

- Para isso, vamos criar um novo script que represente o personagem.

- Vamos codificar o impulso do personagem.

```````cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bird : MonoBehaviour
{
    Rigidbody2D fisica;
       

    private void Awake()
    {
        this.fisica = this.GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            this.fisica.AddForce(Vector2.up * 10, ForceMode2D.Impulse);
        }
    }
}
```````

## Boas práticas de programação

- Arrumar as variáveis fixas anteriores, tanto do persnagem quando dos canos.

- Queremos que nossas variáveis fixas possam ser alteradas dentro da plataforma da unity, sem a necessidade de nenhuma alteração do scirpt.
- É comum que o game design possa fazer alterações na dinâmica do jogo, e muitas vezes ele não tem habilidade necessária para entender os scripts criados pelos programadores.
- Para isso, vamos utilizar o `[SerealizeField]`

``````cs
[SerializeField]
private float force = 10;
// Agora faça  this.force ao invés do valor.
``````

``````cs
[SerializeField]
private float velocity = 0.05f;
// Agora faça  this.velocity ao invés do valor.
``````

- Agora observando no componente de script do personagem e do cano, temos as variáveis que poedm ser alteradas dentro da própria unity, inclusive  em tempo de execução do jogo.

- Execute o jogo e veja.

# Canos infinitos

- De maneira muito simples, podemos fazer uma translação dos canos quando eles saem da cena.

- para isso faça, no script do cano:

``````cs
 if (this.transform.position.x < (-11.01))
        {
            this.transform.position = this.initialPosition;
        }
``````
- Podemos ter uma outra estratégia para criar de fato novos obstáculos, sem a necessidade de apenas reposicionar.


Fim.

# Extra

``````cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class generatepipes : MonoBehaviour
{

    [SerializeField]
    private float timeToCreate;

    private float cron;

    [SerializeField]
    private GameObject prefab;
       

    private void Awake()
    {
        this.cron = this.timeToCreate;
    }
    // Update is called once per frame
    void Update()
    {
        this.cron -= Time.deltaTime;

        if (this.cron < 0)
        {
            GameObject.Instantiate(this.prefab, this.transform.position, Quaternion.identity);
            this.cron = this.timeToCreate;
        }

    }
}

``````
