
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void vuln() {
    char buffer[64];
    printf("Give me plaintext input:\n");
    setbuf(stdout, NULL);
    gets(&buffer);
    fflush(stdout);
}

int main(int argc, char **argv) { vuln(); }