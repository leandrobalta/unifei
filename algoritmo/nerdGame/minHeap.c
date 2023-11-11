#include <stdio.h>
#include <stdlib.h>
#include "minHeap.h"

// Alunos: Leandro Braga - Joao Pedro Renno 
// Matriculas: 2022004250 - 2022010651

#define MAX 1000000


// retorna o pai da posição que voce esta buscando, utiliza a formula passada em aula -> index(atual) / 2, arredondando caso necessario
int PaiMin(int pos){
    return (pos - 1) / 2;
}

// pega o filho da esquerda da posicaum desejada
int EsquerdaMin(int pos){
    return 2 * pos + 1;
}

// pega o filho da direita da posicaum desejada
int DireitaMin(int pos){
    return 2 * pos + 2;
}

void SobeHeapMin(minHeap * Heap, int idx){
    if(idx == 0) return; // caso seja o primeiro elemento

    int pai = PaiMin(idx); // pegando o pai

    // verificando se o filho é menor que o pai para realizar a troca 
    if(Heap->V[idx] < Heap->V[pai]){
        int helper = Heap->V[pai];
        Heap->V[pai] = Heap->V[idx];
        Heap->V[idx] = helper;
        SobeHeapMin(Heap, pai);
    }
    return;
}

void DesceHeapMin(minHeap * Heap, int idx){
    int esq = EsquerdaMin(idx); // pegando o "primeiro" filho desse idx

    if(esq > Heap->n - 1) return; //verifica se o filho da esquerda( no caso o primeiro filho) é o ultimo elemento

    int menorHijo = esq;

    int dir = DireitaMin(idx); // pegando o segundo filho ( no caso o filho da direito)

    if(dir <= Heap->n - 1 && Heap->V[dir] < Heap->V[esq]) menorHijo = dir;

    // se a posicaum analisada for menor do que o seu menor filho, eles trocam de lugar
    if (Heap->V[idx] > Heap->V[menorHijo]){
        int helper = Heap->V[menorHijo];
        Heap->V[menorHijo] = Heap->V[idx];
        Heap->V[idx] = helper;
        DesceHeapMin(Heap, menorHijo);
    }
    return;
}

// aloca espaço na memoria para o hip e para seu vetor de inteiros, com o n iniciando com 0
minHeap * cria_minHeap(){
    minHeap * Heap = (minHeap*) malloc(sizeof(minHeap));
    Heap->V = (int*) malloc(sizeof(int) * MAX);
    Heap->n = 0;
    return Heap;
}

int remove_min(minHeap * H){
    int helper = H->V[0]; // pega a primeira posicaum do vetor
    H->V[0] = H->V[H->n - 1]; // troca o primeiro elemento colocando o ultimo elemento (no caso o maior valor) na primeira posicaum
    H->n = H->n - 1; // diminui o n identificando que o vetor diminui uma unidade
    DesceHeapMin(H, 0);
    return helper;
}

int verifica_min(minHeap * H){
    return H->V[0];
}

void adiciona_elemento_minHeap(minHeap * H, int e){
    H->V[H->n] = e;
    H->n = H->n + 1;
    SobeHeapMin(H, H->n - 1);
}

void constroi_minHeap(minHeap * H){
    for (int i = (H->n - 2); i >= 0; i--)
        DesceHeapMin(H, i);
}

void imprime_minHeap(minHeap * H){
    for (int i = 0; i < H->n; i++)
        printf("%d ", H->V[i]);
    
    printf("\n");
}