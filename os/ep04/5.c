#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sched.h>
#include <sys/resource.h>
#include <sys/types.h>
#include <sys/wait.h>

int child_func(void *arg) {
    printf("Filho: Meu PID = %d\n", getpid());
    // Alterar a prioridade do processo filho
    setpriority(PRIO_PROCESS, 0, 10);
    printf("Filho: Prioridade alterada para 10\n");
    return 0;
}

int main() {
    char child_stack[1024 * 1024];  // Stack do filho
    int flags = CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SIGHAND | CLONE_SYSVSEM | CLONE_PARENT_SETTID | CLONE_CHILD_CLEARTID;
    pid_t child_pid = clone(child_func, child_stack + (1024 * 1024), flags, NULL);

    if (child_pid == -1) {
        perror("Erro ao criar processo filho");
        return 1;
    }

    printf("Pai: Meu PID = %d\n", getpid());
    // Aguardar o processo filho terminar
    waitpid(child_pid, NULL, 0);

    return 0;
}
