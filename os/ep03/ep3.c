#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

#define N 10
#define NUM_FANS 20  // Número de fãs a serem criados

int nFans = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
sem_t dem, fila;

void telefona() {
    // Simula o telefonema para casa
    sleep(rand() % 3 + 1);
    printf("Fã terminou de telefonar e está voltando para assistir novamente.\n");
}

void assisteFilme() {
    // Simula a visualização do filme
    printf("Fã assistindo ao filme.\n");
    sleep(rand() % 4 + 1);
    printf("Fã terminou de assistir e está telefonando para casa.\n");
    telefona();
}

void exibeFilme() {
    // Simula a exibição do filme
    printf("Demonstrador está exibindo o filme.\n");
    sleep(rand() % 4 + 1);
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

    for (int i = 0; i < TOTAL_FANS; i++) {
        if (pthread_create(&fans[i], NULL, fan, NULL) != 0) {
            perror("Erro ao criar um fã");
            exit(1);
        }
    }

    if (pthread_create(&demo, NULL, demonstrator, NULL) != 0) {
        perror("Erro ao criar o demonstrador");
        exit(1);
    }

    for (int i = 0; i < TOTAL_FANS; i++) {
        pthread_join(fans[i], NULL);
    }

    pthread_join(demo, NULL);

    sem_destroy(&dem);
    sem_destroy(&fila);

    return 0;
}
