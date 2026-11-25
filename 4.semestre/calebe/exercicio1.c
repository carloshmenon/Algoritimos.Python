#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int cap = 4;
    int topo = 0;
    char *pilha = malloc(cap);
    char msg[101];

    printf("Mensagem codificada: ");
    scanf("%100s", msg);
    int tam = strlen(msg);

    
    for (int i = 0; i < tam; i++) {
        if (topo == cap) {
            cap *= 2;
            pilha = realloc(pilha, cap);
            printf("(realloc: capacidade agora %d)\n", cap);
        }
        pilha[topo++] = msg[i];
    }

    
    int igual = 1;
    int pos = 0;
    printf("Senha decodificada: ");
    while (topo > 0) {
        char letra = pilha[--topo];
        printf("%c", letra);
        if (letra != msg[pos]) {
            igual = 0;
        }
        pos++;
    }
    printf("\n");

    if (igual)
        printf("Senha espelhada!\n");
    else
        printf("Senha nao espelhada.\n");

    free(pilha);
    return 0;
}
