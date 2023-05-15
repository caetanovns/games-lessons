using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bird : MonoBehaviour
{
    Rigidbody2D fisica;

    [SerializeField]
    private float force = 10;

    private directorscene diretor;

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

    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            this.fisica.velocity = Vector2.zero;
            this.fisica.AddForce(Vector2.up * this.force, ForceMode2D.Impulse);
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        this.fisica.simulated = false;
        this.diretor.FinalizarJogo();
    }
}
