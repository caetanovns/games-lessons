using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pipe : MonoBehaviour
{
    
    [SerializeField]
    private float speed = 0.01f;

    private Vector3 initialPosition;

    private void Awake()
    {
        this.initialPosition = this.transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        this.transform.Translate(Vector2.left * this.speed);
        if (this.transform.position.x < (-11.01))
        {
            this.transform.position = this.initialPosition;
        }
    }
}
