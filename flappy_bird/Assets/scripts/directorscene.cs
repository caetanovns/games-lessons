using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class directorscene : MonoBehaviour
{
    [SerializeField]
    private GameObject imagem;

    private bird passaro;

    private Score score;

    private void Start()
    {
        this.passaro = GameObject.FindObjectOfType<bird>();
        this.score = GameObject.FindObjectOfType<Score>();
    }

    public void FinalizarJogo()
    {
        Time.timeScale = 0;
        this.imagem.SetActive(true);
        
    }

    public void RestartGame()
    {
        this.imagem.SetActive(false);
        Time.timeScale = 1;
        this.passaro.Restart();
        this.score.reiniciar();

        pipe[] pipes = GameObject.FindObjectsOfType<pipe>();
        foreach(pipe p in pipes)
        {
            p.destroy();
        }

    }
}
