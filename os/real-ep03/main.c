/*
Sistemas Operacionais - EP03

Nome: João Lucas Moraes de Oliveira     Matrícula: 2022004242
Nome: Leandro Balta Braga               Matrícula: 2022004260
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#define C 7
#define N 20

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

// DECLARA SEMAFORO PASSAGEIRO
sem_t passageiro;

// DECLARA SEMAFORO CARRINHO
sem_t carrinho;

int Npass = 0;

void *Passageiro(void *arg)
{
    //int id = *(int *)arg;

    while (1)
    {
        pthread_mutex_lock(&mutex);
        Npass++;
        printf("Passageiro %d entrou no carrinho...\n", Npass);
        pthread_mutex_unlock(&mutex);

        sem_post(&carrinho);
        sem_wait(&passageiro);
    }
}

void *Carrinho(void *arg)
{
    while (1)
    {
        while (Npass < C){
            printf("carrinho esperando\n");
            sem_wait(&carrinho);
        }
        pthread_mutex_lock(&mutex);
        printf("carrinho andando\n");
        sleep(2);
        Npass -= C;
        printf("carrinho ja andou\n");
        pthread_mutex_unlock(&mutex);

        for (int i = 0; i < C; i++)
            sem_post(&passageiro);
    }
}

int main(void)
{
    int passageiros_id[N];
    pthread_t passageiros[N];
    pthread_t td1;

    sem_init(&passageiro, 0, C);
    sem_init(&carrinho, 0, 0);

    for (int i = 0; i < N; i++)
    {
        passageiros_id[i] = i + 1;
        pthread_create(&passageiros[i], NULL, Passageiro, NULL);
    }

    pthread_create(&td1, NULL, Carrinho, NULL);

    for (int i = 0; i < N; i++)
    {
        pthread_join(passageiros[i], NULL);
    }

    pthread_join(td1, NULL);

    sem_destroy(&passageiro);
    sem_destroy(&carrinho);

    return 0;
}