#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// João Victor Fernandes Rodrigues - 2020006874
// Leandro Balta Braga - 2022004260

typedef struct
{
    unsigned short dia;
    unsigned short mes;
    unsigned short ano;
    unsigned short hora;
    unsigned short min;
    unsigned short seg;
} data;

typedef struct
{
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


int main(int argc, char *argv[])
{
    FILE *f;
    arquivo a;
    int counter = 1;

    f = fopen("Diretorio.dat", "rb");

    if (!f)
    {
        printf("Não foi possível abrir o arquivo Diretorio.dat\n");
        exit(1);
    }

    while (!feof(f))
    {
        fflush(stdin);
        fread(&a, sizeof(arquivo), 1, f);

        if (argc < 2 || strcmp(argv[1], "") == 0)
        {
            if (a.hidden == 0 && strcmp(a.nome, "0EBH") != 0)
            {
                counter = 0;
                printf("\n");
                printf("%s.%s\n", a.nome, a.extensao);
                counter++;
            }
        }
        else if (strcmp(argv[1], "-a") == 0)
        {
            printf("%s %s %d %d %d %lu %lu\n", a.nome, a.extensao, a.sistema, a.hidden, a.archieved, a.tamanho, a.cluster);
        }
        else if (strcmp(argv[1], "-s") == 0)
        {
            counter = 0;
            printf("\n");
            printf("%s.%s\n", a.nome, a.extensao);
            counter++;
        }
        else if (strcmp(argv[1], "-w") == 0)
        {
            if (a.hidden == 0 && strcmp(a.nome, "") != 0)
            {
                counter = 0;
                printf("%s.%s  ", a.nome, a.extensao);
                counter++;

                if ((counter + 1) % 4 == 0)
                {
                    printf("\n");
                }
            }
        }
        else
        {
            printf("Opção inválida para arq\n");
            break;
        }
    }

    return 0;
}
