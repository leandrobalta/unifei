/*
 * aula08_ex03.c
 * 
 * Copyright 2023 Carlos Minoru Tamaki <minoru@minoru-nitroan51551>
 * 
 */
#include <stdio.h>
#include <unistd.h> /* unix standard routines */
#include <pthread.h> /* pthread functions and data structures */
// Passagem de um valor inteiro
int x=5;
//chamada da thread
pthread_create(&threads[i], NULL, funcao, (void*)&x);
     :
void * funcao ( void * argumentos ){
    int valor = * (int *) argumentos;
    printf("recebi um inteiro: %d \n", valor );
}
