using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ground : MonoBehaviour
{
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
}
