#include <stdio.h> /* standard I/O routines */
#include <unistd.h> /* unix standard routines */
#include <pthread.h> /* pthread functions and data structures */
/* function to be executed by the new thread */
typedef struct time{
    int hour;
    int minute;
} t_time;

void *print_time(void *argumentos) {
    t_time * args = (t_time *)argumentos;
    printf("Agora saum %d:%d, Logo lhe desejo\n", args->hour, args->minute);

    if (args->hour < 13 && args->hour >= 6) printf("Bom dia\n");
    else if (args->hour >13 && (args->hour <= 18 && args->minute <=30)) printf("Boa Tarde\n");
    else printf("Boa noite\n");


    pthread_exit(NULL);
}

int main (int argc, char *argv[]){
    pthread_t thread;
    t_time time;
    scanf("%d", &time.hour);
    scanf("%d", &time.minute);

    pthread_create(&thread, NULL, print_time, (void *)&time);
    pthread_join(thread, NULL);
    return 0;
}