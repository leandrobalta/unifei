#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdnoreturn.h>

// João Victor Fernandes Rodrigues - 2020006874
// Leandro Balta Braga - 2022004260

typedef struct cluster {

    char dados[512];
    unsigned long int prox;

} cluster;

int v_clusters[100];

typedef struct data {

    unsigned short dia;
    unsigned short mes;
    unsigned short ano;
    unsigned short hora;
    unsigned short min;
    unsigned short seg;

} data;

typedef struct arquivos {

    char nome[8]; //nome do arquivo iniciado com o hexadecimal 0ebh são arquivos deletados
    char extensao[3];
    // Proteção
    unsigned short sistema; //arquivo do sistema
    unsigned short hidden; //arquivo oculto
    unsigned short archieved; //arquivo arquivado
    // Data e hora da criação
    data criacao;
    // Data do último acesso
    data acesso;
    // Tamanho
    unsigned long int tamanho;
    // Cluster inicial
    unsigned long int cluster;

} arquivo;

void readCluster(FILE *arq, int cluster_atual, int *qtd_cluster, unsigned long int *tam_arq) {
    cluster ctr;
    fseek(arq, sizeof(cluster) * cluster_atual, SEEK_SET);
    fread(&ctr, sizeof(cluster), 1, arq);
    v_clusters[*qtd_cluster] = cluster_atual;

    if (ctr.prox) {
        cluster_atual = ctr.prox;
        (*qtd_cluster)++;
        for (int i = 0; i < 512; i++) {
            putchar(ctr.dados[i]);
        }
        (*tam_arq) -= 512;
        readCluster(arq, cluster_atual, qtd_cluster, tam_arq);
    } else {
        (*qtd_cluster)++;
        for (int i = 0; i < *tam_arq; i++) {
            putchar(ctr.dados[i]);
        }
    }
}

int main() {
    FILE *arq;
    arquivo a, arq_ext4;
    int qtd_cluster = 0;
    arq = fopen("Disco.dat", "rb");

    if (!arq) {
        printf("Não foi possível abrir o arquivo Disco.dat\n");
        exit(1);
    }

    while (fread(&a, sizeof(arquivo), 1, arq) == 1) {
        if (!strcmp(a.nome, "EXT4") && !strcmp(a.extensao, "TXT")) {
            arq_ext4 = a;
            break;
        }
    }

    unsigned long int cluster_atual = arq_ext4.cluster;
    unsigned long int tam_arq = arq_ext4.tamanho;

    if (cluster_atual > 0 && tam_arq > 0) {
        readCluster(arq, cluster_atual, &qtd_cluster, &tam_arq);
    }

    printf("Quantidade de clusters: %d\n", qtd_cluster);
    printf("Tamanho do arquivo: %lu\n", arq_ext4.tamanho);
    fclose(arq);
}
