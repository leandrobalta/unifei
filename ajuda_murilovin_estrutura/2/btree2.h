#ifndef BTREE_H
#define BTREE_H

#define T 4  // Grau mínimo (T pode ser ajustado)

typedef struct {
    char nome[50];
    char cpf[11];
    char curso[50];
    int matricula;
} Registro;

typedef struct NoArvoreB {
    int n;
    int folha;
    Registro registros[2*T-1];
    struct NoArvoreB *C[2*T];
} NoArvoreB;

typedef struct {
    NoArvoreB *raiz;
} ArvoreB;

ArvoreB* criarArvoreB();
NoArvoreB* criarNo(int folha);
void criarIndice(ArvoreB *arvore, const char *nomeArquivo);
int buscarElemento(NoArvoreB *no, int matricula);
void buscarNoArquivo(const char *nomeArquivo, int linha);
void remover(ArvoreB *arvore, int matricula);
void inserir(ArvoreB *arvore, Registro registro);
void inserirNaoCheio(NoArvoreB *no, Registro registro);
void dividirFilho(NoArvoreB *x, int i);
int buscarChave(NoArvoreB *no, int matricula);
void removerChave(NoArvoreB *no, int matricula);
void removerDeFolha(NoArvoreB *no, int idx);
void removerDeNaoFolha(NoArvoreB *no, int idx);
void preencher(NoArvoreB *no, int idx);
void emprestarDoAnterior(NoArvoreB *no, int idx);
void emprestarDoProximo(NoArvoreB *no, int idx);
void fundir(NoArvoreB *no, int idx);
int getPredecessor(NoArvoreB *no, int idx);
int getSucessor(NoArvoreB *no, int idx);

#endif