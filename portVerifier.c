#include <stdio.h>
#include <netdb.h>

int main(int argc, char *argv[]){
    int mysocket;
    int conn;

    struct sockaddr_in target;
    mysocket = socket(AF_INET, SOCK_STREAM,0); // 0 -> ip protocol
    target.sin_family = AF_INET;
    target.sin_port = htons(argv[2]);
    target.sin_addr.s_addr = inet_addr(argv[1]); 

    conn = connect(mysocket, (struct sockaddr *)&target, sizeof target);
    if(conn == 0){
        printf("port is open\n");
        close(mysocket);
        close(conn);
    }else{
        printf("port is closed\n");
        close(mysocket);
        close(conn);
    }
}
