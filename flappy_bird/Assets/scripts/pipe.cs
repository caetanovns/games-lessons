using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pipe : MonoBehaviour
{
    
    [SerializeField]
    private float speed = 0.01f;


    private void Awake()
    {
        this.transform.Translate(Vector3.up * Random.Range(-1.5f,1.5f));
    }

    // Update is called once per frame
    void Update()
    {
        this.transform.Translate(Vector2.left * this.speed * Time.deltaTime);
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
