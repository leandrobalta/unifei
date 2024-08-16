#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 512

typedef struct {
    char nome[50];
    char cpf[12];  // CPF tem 11 dígitos + 1 caractere nulo
    char curso[50];
    int matricula;
} Registro;

// Função para dividir uma string por um delimitador e retornar um array de strings
char **split_line(char *line, const char *delimiter, int *num_tokens) {
    char **tokens = NULL;
    char *token;
    int count = 0;

    // Faz uma cópia da linha para não modificar a linha original
    char *line_copy = strdup(line);

    token = strtok(line_copy, delimiter);
    while (token != NULL) {
        tokens = realloc(tokens, sizeof(char *) * (count + 1));
        tokens[count] = strdup(token);  // Duplica o token para preservar o valor
        count++;
        token = strtok(NULL, delimiter);
    }

    *num_tokens = count;
    free(line_copy);  // Libera a memória da linha copiada
    return tokens;
}

int main() {
    FILE *file = fopen("unifei.txt", "r");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        return EXIT_FAILURE;
    }

    char line[MAX_LINE_LENGTH];

    // Lê e processa cada linha do arquivo CSV
    while (fgets(line, sizeof(line), file)) {
        // Remove o caractere de nova linha, se houver
        line[strcspn(line, "\n")] = 0;

        int num_tokens;
        char **tokens = split_line(line, ",", &num_tokens);

        if (num_tokens == 4) {
            Registro registro;

            strncpy(registro.nome, tokens[0], sizeof(registro.nome) - 1);
            registro.nome[sizeof(registro.nome) - 1] = '\0';  // Garantir terminação nula

            strncpy(registro.cpf, tokens[1], sizeof(registro.cpf) - 1);
            registro.cpf[sizeof(registro.cpf) - 1] = '\0';  // Garantir terminação nula

            strncpy(registro.curso, tokens[2], sizeof(registro.curso) - 1);
            registro.curso[sizeof(registro.curso) - 1] = '\0';  // Garantir terminação nula

            registro.matricula = atoi(tokens[3]);

            // Printando os valores para verificar
            printf("Nome: %s\n", registro.nome);
            printf("CPF: %s\n", registro.cpf);
            printf("Curso: %s\n", registro.curso);
            printf("Matrícula: %d\n", registro.matricula);
        } else {
            printf("Número de tokens inesperado: %d\n", num_tokens);
        }

        for (int i = 0; i < num_tokens; i++) {
            free(tokens[i]);  // Libera a memória de cada token
        }
        free(tokens);  // Libera a memória do array de tokens
    }

    fclose(file);
    return EXIT_SUCCESS;
}
