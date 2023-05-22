using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    private int pontos;

    [SerializeField]
    private Text texto;

    private AudioSource audio;

    public void Awake()
    {
        this.audio = this.GetComponent<AudioSource>();
    }

    public void adicionar()
    {
        this.pontos++;
        this.texto.text = this.pontos.ToString();
        this.audio.Play();
    }

    public void reiniciar()
    {
        this.pontos = 0;
        this.texto.text = this.pontos.ToString();
    }
}
