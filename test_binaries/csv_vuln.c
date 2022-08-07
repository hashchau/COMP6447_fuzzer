#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* getfield(char* line, int num)
{
    char* tok = strtok(line, ",");
    if (!--num) {
            return tok;
    }
    while ((tok = strtok(NULL, ",")) != NULL) {
        if (!--num) {
            return tok;
        }
    }
    return NULL;
}

int main()
{
    char line[1024];
    for(int i = 0; i < 2; i++){
        fgets(line, 1024, stdin);
        char* tmp = strdup(line);
        int num = atoi(getfield(tmp, 2));
        printf("%d\n", atoi(getfield(tmp, num)));
        free(tmp);
    }
}
