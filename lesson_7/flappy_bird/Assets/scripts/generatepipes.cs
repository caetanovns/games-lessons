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
