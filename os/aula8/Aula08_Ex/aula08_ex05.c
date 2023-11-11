/*
 * aula08_ex05.c
 * 
 * Copyright 2023 Carlos Minoru Tamaki <minoru@minoru-nitroan51551>
 * 
 */
#include <stdio.h>
#include <unistd.h> /* unix standard routines */
#include <pthread.h> /* pthread functions and data structures */
// Passagem de múltiplos parâmetros usando uma estrutura
int x=5 ; float y=2.5
typedef struct { int a; float b; } ST;
ST v;
v.a=x; v.b=y;
pthread_create(&threads[i], NULL, funcao, (void*)&v);
     :
void * funcao ( void * argumentos ){
    ST * in = (ST *) argumentos ;
    printf("recebi dois valores: %d %f ", in->a, in->b );
}
