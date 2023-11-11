// Aluno - Matricula
// Leandro Balta Braga - 2022004260
// xxxx - yyyy

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

#define N 10
#define TOTAL_FANS 30

int nFans = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
sem_t dem, fila;


void telefona() {
    sleep(1);
    printf("fan already called, now will watch again\n");
}

void assisteFilme() {
    printf("fan watching the movie\n");
    sleep(1);
    printf("fan already watched, now will call");
    telefona();
}


void exibeFilme() {
    printf("Demonstrador está exibindo o filme.\n");
    sleep(1);
    printf("Demonstrador terminou de exibir o filme.\n");
}

void *fan(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        nFans++;
        printf("Chegou um novo fã. Total de fãs: %d.\n", nFans);
        pthread_mutex_unlock(&mutex);
        sem_post(&dem);
        sem_wait(&fila);
        assisteFilme();
        telefona();
    }
}

void *demonstrator(void *arg) {
    while (1) {
        while (nFans < N)
            sem_wait(&dem);

        pthread_mutex_lock(&mutex);
        nFans -= N;
        pthread_mutex_unlock(&mutex);

        for (int i = 0; i < N; i++)
            sem_post(&fila);

        exibeFilme();
    }
}

int main() {
    pthread_t fans[TOTAL_FANS];
    pthread_t demo;

    sem_init(&dem, 0, 0);
    sem_init(&fila, 0, 0);
    
    int result = pthread_create(&demo, NULL, demonstrator, NULL);
    if (result != 0) {
        perror("Error creating demonstrator thread.");
        exit(1);
    }

    for (int i = 0; i < TOTAL_FANS; i++) {
        int result = pthread_create(&fans[i], NULL, fan, NULL);

        if (result != 0) {
            perror("Error creating fans thread.");
            exit(1);
        }
    }

    for (int i = 0; i < TOTAL_FANS; i++) {
        pthread_join(fans[i], NULL);
    }
    pthread_join(demo, NULL);

    sem_destroy(&dem);
    sem_destroy(&fila);

    return 0;
}


