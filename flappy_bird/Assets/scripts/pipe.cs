using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pipe : MonoBehaviour
{
    
    [SerializeField]
    private float speed = 0.01f;

    private Vector3 positionBird;
    private bool point = false;

    private Score score;

     
    private void Awake()
    {
        this.transform.Translate(Vector3.up * Random.Range(-1.5f,1.5f));
    }

    private void Start()
    {
        this.positionBird = GameObject.FindObjectOfType<bird>().transform.position;
        this.score = GameObject.FindObjectOfType<Score>();
    }

    // Update is called once per frame
    void Update()
    {
        this.transform.Translate(Vector2.left * this.speed * Time.deltaTime);

        if (!this.point && this.transform.position.x < this.positionBird.x)
        {
            this.point = true;
            this.score.adicionar();
        }
    }

    private void OnTriggerEnter2D(Collider2D collider)
    {
        this.destroy();
    }

    public void destroy()
    {
        GameObject.Destroy(this.gameObject);
    }
}
