#include <stdio.h>   /* Rotinas padrão de I/O */
#include <unistd.h>  /* Rotinas padrão do Unix */
#include <pthread.h> /* Funções e estruturas de dados do pthread */

/* Função a ser executada pela nova thread */

typedef struct Argumentos
{
    int inicio, fim, resultado;
} T_Argumentos;

void *soma(void *argumentos)
{
    T_Argumentos *args = (T_Argumentos *)argumentos;
    int soma = 0;
    int inicio = args->inicio;
    int fim = args->fim;

    for (int i = inicio; i <= fim; i++)
    {
        if (args->resultado % 2 == i % 2)
        {
            soma += i;
        }
    }
    args->resultado = soma;
    return NULL;
}

int main()
{
    // Transforme isso em um array de threads
    pthread_t thread1, thread2;
    int inicio, fim;

    scanf("%d", &inicio);
    scanf("%d", &fim);

    T_Argumentos *somaPar = (T_Argumentos *)malloc(sizeof(T_Argumentos));
    somaPar->inicio = inicio;
    somaPar->fim = fim;
    somaPar->resultado = 0;

    T_Argumentos *somaImpar = (T_Argumentos *)malloc(sizeof(T_Argumentos));
    somaImpar->inicio = inicio;
    somaImpar->fim = fim;
    somaImpar->resultado = 0;

    pthread_create(&thread1, NULL, soma, (void *)somaPar);

    pthread_create(&thread2, NULL, soma, (void *)somaImpar);

    pthread_join(thread1, NULL);

    pthread_join(thread2, NULL);

    printf("Principal: Soma dos números pares = %d\n", somaPar->resultado);

    printf("Principal: Soma dos números ímpares = %d\n", somaImpar->resultado);

    printf("Principal: Saindo...\n");

    free(somaPar);
    free(somaImpar);

    return 0;
}
