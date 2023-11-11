#include <sys/resource.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t child_pid;

    child_pid = fork();

    if (child_pid == 0) {
        // Processo filho
        printf("Filho: Meu PID = %d\n", getpid());
        // Alterar a prioridade do processo filho
        setpriority(PRIO_PROCESS, 0, 10);
        printf("Filho: Prioridade alterada para 10\n");
    } else if (child_pid > 0) {
        // Processo pai
        printf("Pai: Meu PID = %d\n", getpid());
        // Aguardar o processo filho terminar
        wait(NULL);
    } else {
        // Erro na criação do processo filho
        perror("Erro ao criar processo filho");
        return 1;
    }

    return 0;
}