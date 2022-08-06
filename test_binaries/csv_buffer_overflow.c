#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <csv.h>

void vuln() {
    char buffer[64];
    printf("Give me CSV input:\n");
    setbuf(stdout, NULL);
    gets(&buffer);
    fflush(stdout);
}

int main(int argc, char **argv) {
    vuln();
}