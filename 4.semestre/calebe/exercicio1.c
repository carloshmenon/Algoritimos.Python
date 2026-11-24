#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *dados;
    int topo;
    int cap;
} Pilha;

void empilhar(Pilha *p, char c) {
    if (p->topo == p->cap) {
        p->cap = p->cap * 2;
        p->dados = realloc(p->dados, p->cap * sizeof(char));
        printf("(realloc: capacidade agora %d)\n", p->cap);
    }
    p->dados[p->topo] = c;
    p->topo++;
}

char desempilhar(Pilha *p) {
    p->topo--;
    return p->dados[p->topo];
}

int main() {
    Pilha p;
    p.cap = 4;
    p.topo = 0;
    p.dados = malloc(p.cap * sizeof(char));

    char msg[101];
    char senha[101];
    int i, n = 0;

    printf("Mensagem codificada: ");
    scanf("%100s", msg);

    for (i = 0; msg[i] != '\0'; i++) {
        empilhar(&p, msg[i]);
    }

    printf("Senha decodificada: ");
    while (p.topo > 0) {
        senha[n] = desempilhar(&p);
        printf("%c", senha[n]);
        n++;
    }
    senha[n] = '\0';
    printf("\n");

    if (strcmp(msg, senha) == 0) {
        printf("Senha espelhada!\n");
    } else {
        printf("Senha nao espelhada.\n");
    }

    free(p.dados);
    return 0;
}
