#include<stdio.h>
#include<string.h>

int main( int argc, char* argv[]){
    int notAllowed = 0;
    char buffer[8];
    strcpy(buffer, argv[1]);
    if(notAllowed == 0){
        printf("[!] Access Denied\n");
    }else{
        printf("[*] Access Granted ! \n"); 
    }
    

}