using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bird : MonoBehaviour
{
    Rigidbody2D fisica;

    [SerializeField]
    private float force = 10;

    private void Awake()
    {
        this.fisica = this.GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            this.fisica.AddForce(Vector2.up * this.force, ForceMode2D.Impulse);
        }
    }
}
