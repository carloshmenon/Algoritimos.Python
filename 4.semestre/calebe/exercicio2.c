#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int numero;
    char cliente[50];
    char item[50];
} Pedido;

typedef struct {
    Pedido *dados;
    int inicio, n, cap;
} FilaPed;

int main() {
    FilaPed f;
    f.cap = 5;
    f.inicio = 0;
    f.n = 0;
    f.dados = malloc(f.cap * sizeof(Pedido));

    int opcao, proximo = 1;

    do {
        printf("\n1 - Novo pedido\n2 - Entregar proximo\n3 - Mostrar fila\n0 - Sair\nOpcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            if (f.n == f.cap) {
                printf("Balcao lotado!\n");
            } else {
                int fim = (f.inicio + f.n) % f.cap;
                f.dados[fim].numero = proximo;
                printf("Cliente: ");
                scanf(" %49[^\n]", f.dados[fim].cliente);
                printf("Item: ");
                scanf(" %49[^\n]", f.dados[fim].item);
                printf("Pedido #%d registrado.\n", proximo);
                proximo++;
                f.n++;
            }
        } else if (opcao == 2) {
            if (f.n == 0) {
                printf("Nao ha pedidos na fila.\n");
            } else {
                Pedido p = f.dados[f.inicio];
                printf("Entregue: #%d %s - %s\n", p.numero, p.cliente, p.item);
                f.inicio = (f.inicio + 1) % f.cap;
                f.n--;
            }
        } else if (opcao == 3) {
            if (f.n == 0) {
                printf("Fila vazia.\n");
            }
            for (int i = 0; i < f.n; i++) {
                int p = (f.inicio + i) % f.cap;
                printf("#%d %s - %s\n", f.dados[p].numero,
                       f.dados[p].cliente, f.dados[p].item);
            }
        } else if (opcao != 0) {
            printf("Opcao invalida.\n");
        }
    } while (opcao != 0);

    free(f.dados);
    return 0;
}
