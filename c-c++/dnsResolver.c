#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/types.h>

int main( int argc, char *argv[]){
	char *target;
	target = argv[1];
	struct hostent *host;
	char *result;
	char *word[50];
	FILE *dict;
	dict = fopen(argv[2],"r");
	if(argc < 2){
		printf("[*] ONE DNS RESOLVER TO RULE THEM ALL [*]\n You must provide an target and a file with your words\n ./dnsResolv target.com dict.txt");
	}else{	
		while(fscanf(dict, "%s", &word) != EOF){
			result = (char *) strcat(word, target);
			host = gethostbyname(result);
			if(host != NULL){
				printf("%s :::> %s\n", target, inet_ntoa(*((struct in_addr *)host->h_addr)));
				return -1;
			}
		}
	}
}

