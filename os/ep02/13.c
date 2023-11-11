#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdint.h>
#define _GNU_SOURCE

void *calcularMedia(void *entrada)
{
    int *array = (int *)entrada;
    int media = 0;

    for (int i = 0; i < 20; i++)
    {
        media += array[i];
    }

    media /= 20;

    return (void *)(intptr_t)media;
}

void *calcularMediana(void *entrada)
{
    int *array = (int *)entrada;
    int arrayOrdenado[20];

    for (int i = 0; i < 20; i++)
    {
        arrayOrdenado[i] = array[i];
    }

    // Ordena o vetor
    for (int i = 0; i < 19; i++)
    {
        for (int j = 0; j < 19 - i; j++)
        {
            if (arrayOrdenado[j] > arrayOrdenado[j + 1])
            {
                int temp = arrayOrdenado[j];
                arrayOrdenado[j] = arrayOrdenado[j + 1];
                arrayOrdenado[j + 1] = temp;
            }
        }
    }

    int mediana;
    if (20 % 2 == 0)
    {
        mediana = (arrayOrdenado[9] + arrayOrdenado[10]) / 2;
    }
    else
    {
        mediana = arrayOrdenado[10];
    }

    return (void *)(intptr_t)mediana;
}

int main()
{
    int array[20];
    int media = 0;
    int mediana = 0;

    srand(time(NULL));

    for (int i = 0; i < 20; i++)
    {
        array[i] = rand() % 100;
    }

    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, calcularMedia, (void *)array);
    pthread_create(&thread2, NULL, calcularMediana, (void *)array);

    pthread_join(thread1, (void *)&media);
    pthread_join(thread2, (void *)&mediana);

    printf("Média: %d\n", media);
    printf("Mediana: %d\n", mediana);

    return 0;
}
