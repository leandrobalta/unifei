#include <stdlib.h> // malloc()
#include <pthread.h>
#define _GNU_SOURCE // para acesso a definições específicas do Linux
#include <stdlib.h> // malloc()
#include <stdint.h> // intptr_t
#include <unistd.h> // getpid(), gettid()
#include <sched.h>  // clone(), flags
#include <stdio.h>
#include <math.h>

void *calcularMedia(void *entrada) {

    int *array = (int *)entrada;
    int media = 0;

    for (int i = 0; i < 20; i++) {
        media += array[i];
    }

    media /= 20;

    return (void *)media;

}

void *calcularDesvioPadrao(void *entrada) {

    int *array = (int *)entrada;
    int media = 0;
    int desvioPadrao = 0;

    for (int i = 0; i < 20; i++) {
        media += array[i];
    }

    media /= 20;

    for (int i = 0; i < 20; i++) {
        desvioPadrao += (array[i] - media) * (array[i] - media);
    }

    desvioPadrao /= 20;

    desvioPadrao = sqrt(desvioPadrao);

    return (void *)desvioPadrao;

}

int main() {

    int array[20];
    int media = 0;
    int desvioPadrao = 0;

    // Torna o array verdadeiramente aleatório
    srand(time(NULL));

    for (int i = 0; i < 20; i++) {
        array[i] = rand() % 100;
    }

    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, calcularMedia, (void *)array);
    pthread_create(&thread2, NULL, calcularDesvioPadrao, (void *)array);

    pthread_join(thread1, (void *)&media);
    pthread_join(thread2, (void *)&desvioPadrao);

    printf("Média: %d\n", media);
    printf("Desvio Padrão: %d\n", desvioPadrao);

    return 0;

}
