#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    char c = 'a';
    pid_t pid;

    if ((pid = fork()) < 0)
    {
        perror("fork");
        exit(1);
    }
    if (pid == 0)
    {
        c = 'b';
        printf("Caractere e Endereco: %c - %p (filho)\n",c,&c);
    }
    else
    {
        c='b';
        printf("Caractere e Endereco: %c - %p (pai)\n",c,&c);
    }

	return 0;
}
