#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int pid = 0;
    int pidpai, pidfilho;
    pidpai = getpid();
    pid = fork();
    if (pid != 0)
    {
        printf("Sou processo pai!!! Meu PID é %d\n", pidpai);
    }
    else
    {
        pidfilho = getpid();
        printf("Sou processo filho!!! Meu PID é %d e o PID do meu pai é %d\n", pidfilho,
               pidpai);
    }
    return 0;
}