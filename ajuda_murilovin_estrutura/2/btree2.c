#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "btree2.h"

// Função para criar uma árvore B
ArvoreB* criarArvoreB() {
    ArvoreB *arvore = (ArvoreB*)malloc(sizeof(ArvoreB));
    if (!arvore) {
        printf("Erro ao alocar memória para a árvore\n");
        exit(EXIT_FAILURE);
    }
    arvore->raiz = criarNo(1);
    return arvore;
}

// Função para criar um nó da árvore B
NoArvoreB* criarNo(int folha) {
    NoArvoreB *no = (NoArvoreB*)malloc(sizeof(NoArvoreB));
    if (!no) {
        printf("Erro ao alocar memória para o nó\n");
        exit(EXIT_FAILURE);
    }
    no->folha = folha;
    no->n = 0;
    for (int i = 0; i < 2*T; i++) {
        no->C[i] = NULL;
    }
    return no;
}

// Função para criar o índice a partir de um arquivo
void criarIndice(ArvoreB *arvore, const char *nomeArquivo) {
    FILE *arquivo = fopen(nomeArquivo, "r");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo\n");
        return;
    }

    char linha[200]; // Tamanho arbitrário para ler cada linha do arquivo
    int posicao = 0;
    while (fgets(linha, sizeof(linha), arquivo)) {
        char *nome = strtok(linha, ",");
        char *cpf = strtok(NULL, ",");
        char *curso = strtok(NULL, ",");
        char *matricula_str = strtok(NULL, ",");

        if (nome && cpf && curso && matricula_str) {
            Registro registro;
            strncpy(registro.nome, nome, sizeof(registro.nome) - 1);
            strncpy(registro.cpf, cpf, sizeof(registro.cpf) - 1);
            strncpy(registro.curso, curso, sizeof(registro.curso) - 1);
            registro.matricula = atoi(matricula_str);

            inserir(arvore, registro);
            posicao++;
        }
    }

    fclose(arquivo);
    printf("Total de registros lidos: %d\n", posicao);  // Mensagem de depuração
    printf("Índice criado a partir do arquivo %s.\n", nomeArquivo);
}

// Função para inserir um registro na árvore B
void inserir(ArvoreB *arvore, Registro registro) {
    NoArvoreB *r = arvore->raiz;
    if (r->n == 2*T - 1) {
        NoArvoreB *s = criarNo(0);
        arvore->raiz = s;
        s->C[0] = r;
        dividirFilho(s, 0);
        inserirNaoCheio(s, registro);
    } else {
        inserirNaoCheio(r, registro);
    }
}

// Função para inserir um registro em um nó não cheio
void inserirNaoCheio(NoArvoreB *no, Registro registro) {
    int i = no->n - 1;

    if (no->folha) {
        while (i >= 0 && registro.matricula < no->registros[i].matricula) {
            no->registros[i + 1] = no->registros[i];
            i--;
        }
        no->registros[i + 1] = registro;
        no->n++;
    } else {
        while (i >= 0 && registro.matricula < no->registros[i].matricula) {
            i--;
        }
        i++;
        if (no->C[i]->n == 2*T - 1) {
            dividirFilho(no, i);
            if (registro.matricula > no->registros[i].matricula) {
                i++;
            }
        }
        inserirNaoCheio(no->C[i], registro);
    }
}

// Função para dividir um filho
void dividirFilho(NoArvoreB *x, int i) {
    NoArvoreB *z = criarNo(x->C[i]->folha);
    NoArvoreB *y = x->C[i];
    z->n = T - 1;

    for (int j = 0; j < T-1; j++) {
        z->registros[j] = y->registros[j + T];
    }

    if (!y->folha) {
        for (int j = 0; j < T; j++) {
            z->C[j] = y->C[j + T];
        }
    }

    y->n = T - 1;

    for (int j = x->n; j >= i + 1; j--) {
        x->C[j + 1] = x->C[j];
    }

    x->C[i + 1] = z;

    for (int j = x->n - 1; j >= i; j--) {
        x->registros[j + 1] = x->registros[j];
    }

    x->registros[i] = y->registros[T - 1];
    x->n++;
}

// Função para buscar um elemento na árvore B
int buscarElemento(NoArvoreB *no, int matricula) {
    int i = 0;
    while (i < no->n && matricula > no->registros[i].matricula) {
        i++;
    }

    if (i < no->n && matricula == no->registros[i].matricula) {
        return i;  // Retorna o índice do registro encontrado
    }

    if (no->folha) {
        return -1;  // Retorna -1 se não encontrou e é uma folha
    } else {
        return buscarElemento(no->C[i], matricula);  // Busca recursivamente nos filhos
    }
}

// Função para buscar um registro no arquivo pelo número da linha
void buscarNoArquivo(const char *nomeArquivo, int linha) {
    FILE *arquivo = fopen(nomeArquivo, "r");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo\n");
        return;
    }

    Registro registro;
    fseek(arquivo, linha * sizeof(Registro), SEEK_SET);
    fread(&registro, sizeof(Registro), 1, arquivo);

    printf("Registro encontrado: %s, %s, %s, \n", registro.nome, registro.cpf, registro.curso);

    fclose(arquivo);
}

// Função para remover um registro da árvore B
void remover(ArvoreB *arvore, int matricula) {
    if (!arvore->raiz) {
        printf("A árvore está vazia\n");
        return;
    }

    removerChave(arvore->raiz, matricula);

    if (arvore->raiz->n == 0) {
        NoArvoreB *tmp = arvore->raiz;
        if (arvore->raiz->folha) {
            arvore->raiz = NULL;
        } else {
            arvore->raiz = arvore->raiz->C[0];
        }
        free(tmp);
    }
}

// Função para remover uma chave da árvore B
void removerChave(NoArvoreB *no, int matricula) {
    int idx = buscarChave(no, matricula);

    if (idx < no->n && no->registros[idx].matricula == matricula) {
        if (no->folha) {
            removerDeFolha(no, idx);
        } else {
            removerDeNaoFolha(no, idx);
        }
    } else {
        if (no->folha) {
            printf("A matrícula %d não está na árvore\n", matricula);
            return;
        }

        int flag = (idx == no->n);

        if (no->C[idx]->n < T) {
            preencher(no, idx);
        }

        if (flag && idx > no->n) {
            removerChave(no->C[idx - 1], matricula);
        } else {
            removerChave(no->C[idx], matricula);
        }
    }
}

// Função para remover de um nó folha
void removerDeFolha(NoArvoreB *no, int idx) {
    for (int i = idx + 1; i < no->n; ++i) {
        no->registros[i - 1] = no->registros[i];
    }

    no->n--;
}

// Função para remover de um nó não folha
void removerDeNaoFolha(NoArvoreB *no, int idx) {
    Registro k = no->registros[idx];

    if (no->C[idx]->n >= T) {
        int pred = getPredecessor(no, idx);
        removerChave(no->C[idx], pred);
        no->registros[idx] = no->C[idx]->registros[no->C[idx]->n - 1]; // Atualiza a chave com a última chave do nó
    } else if (no->C[idx + 1]->n >= T) {
        int succ = getSucessor(no, idx);
        removerChave(no->C[idx + 1], succ);
        no->registros[idx] = no->C[idx + 1]->registros[0]; // Atualiza a chave com a primeira chave do nó
    } else {
        fundir(no, idx);
        removerChave(no->C[idx], k.matricula);
    }
}

// Função para preencher um nó filho que tem menos que T chaves
void preencher(NoArvoreB *no, int idx) {
    if (idx != 0 && no->C[idx - 1]->n >= T) {
        emprestarDoAnterior(no, idx);
    } else if (idx != no->n && no->C[idx + 1]->n >= T) {
        emprestarDoProximo(no, idx);
    } else {
        if (idx != no->n) {
            fundir(no, idx);
        } else {
            fundir(no, idx - 1);
        }
    }
}

// Função para pegar emprestado de um nó anterior
void emprestarDoAnterior(NoArvoreB *no, int idx) {
    NoArvoreB *filho = no->C[idx];
    NoArvoreB *irmao = no->C[idx - 1];

    for (int i = filho->n - 1; i >= 0; --i) {
        filho->registros[i + 1] = filho->registros[i];
    }

    if (!filho->folha) {
        for (int i = filho->n; i >= 0; --i) {
            filho->C[i + 1] = filho->C[i];
        }
    }

    filho->registros[0] = no->registros[idx - 1];

    if (!filho->folha) {
        filho->C[0] = irmao->C[irmao->n];
    }

    no->registros[idx - 1] = irmao->registros[irmao->n - 1];

    filho->n += 1;
    irmao->n -= 1;
}

// Função para pegar emprestado de um nó próximo
void emprestarDoProximo(NoArvoreB *no, int idx) {
    NoArvoreB *filho = no->C[idx];
    NoArvoreB *irmao = no->C[idx + 1];

    filho->registros[filho->n] = no->registros[idx];

    if (!filho->folha) {
        filho->C[filho->n + 1] = irmao->C[0];
    }

    no->registros[idx] = irmao->registros[0];

    for (int i = 1; i < irmao->n; ++i) {
        irmao->registros[i - 1] = irmao->registros[i];
    }

    if (!irmao->folha) {
        for (int i = 1; i <= irmao->n; ++i) {
            irmao->C[i - 1] = irmao->C[i];
        }
    }

    filho->n += 1;
    irmao->n -= 1;
}

// Função para fundir dois nós
void fundir(NoArvoreB *no, int idx) {
    NoArvoreB *filho = no->C[idx];
    NoArvoreB *irmao = no->C[idx + 1];

    filho->registros[T - 1] = no->registros[idx];

    for (int i = 0; i < irmao->n; ++i) {
        filho->registros[i + T] = irmao->registros[i];
    }

    if (!filho->folha) {
        for (int i = 0; i <= irmao->n; ++i) {
            filho->C[i + T] = irmao->C[i];
        }
    }

    for (int i = idx + 1; i < no->n; ++i) {
        no->registros[i - 1] = no->registros[i];
    }

    for (int i = idx + 2; i <= no->n; ++i) {
        no->C[i - 1] = no->C[i];
    }

    filho->n += irmao->n + 1;
    no->n--;

    free(irmao);
}

// Função para obter o predecessor de um nó
int getPredecessor(NoArvoreB *no, int idx) {
    NoArvoreB *atual = no->C[idx];
    while (!atual->folha) {
        atual = atual->C[atual->n];
    }
    return atual->registros[atual->n - 1].matricula;
}

// Função para obter o sucessor de um nó
int getSucessor(NoArvoreB *no, int idx) {
    NoArvoreB *atual = no->C[idx + 1];
    while (!atual->folha) {
        atual = atual->C[0];
    }
    return atual->registros[0].matricula;
}

// Função para buscar uma chave em um nó
int buscarChave(NoArvoreB *no, int matricula) {
    int idx = 0;
    while (idx < no->n && matricula > no->registros[idx].matricula) {
        ++idx;
    }
    return idx;
}