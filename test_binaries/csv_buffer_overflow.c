#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <csv.h>

void vuln() {
    int result = 0;
    struct csv_parser *p = NULL;
    char buffer[64];
    printf("Give me CSV input:\n");
    setbuf(stdout, NULL);
    gets(&buffer);
    fflush(stdout);
}

int main(int argc, char **argv) {
    vuln();
}