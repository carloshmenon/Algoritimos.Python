#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int numero;
    char cliente[50];
    char item[50];
} Pedido;

int main() {
    int cap = 5;
    Pedido *fila = malloc(cap * sizeof(Pedido));
    int inicio = 0;   
    int fim = 0;      
    int qtd = 0;      
    int contador = 1;
    int opcao;
    int j;

    do {
        printf("\n1 - Novo pedido\n2 - Entregar proximo\n3 - Mostrar fila\n0 - Sair\nOpcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (qtd == cap) {
                    printf("Balcao lotado!\n");
                    break;
                }
                fila[fim].numero = contador;
                printf("Cliente: ");
                scanf(" %49[^\n]", fila[fim].cliente);
                printf("Item: ");
                scanf(" %49[^\n]", fila[fim].item);
                printf("Pedido #%d registrado.\n", contador);

                contador++;
                qtd++;
                fim++;
                if (fim == cap) fim = 0; 
                break;

            case 2:
                if (qtd == 0) {
                    printf("Nao ha pedidos na fila.\n");
                    break;
                }
                printf("Pedido #%d — %s — %s entregue\n", fila[inicio].numero,
                       fila[inicio].cliente, fila[inicio].item);
                qtd--;
                inicio++;
                if (inicio == cap) inicio = 0;
                break;

            case 3:
                if (qtd == 0) {
                    printf("Fila vazia.\n");
                }
                if (qtd == cap) {
                    printf("Balcao lotado!\n");
                }
                j = inicio;
                for (int k = 0; k < qtd; k++) {
                    printf("#%d %s - %s\n", fila[j].numero, fila[j].cliente, fila[j].item);
                    j++;
                    if (j == cap) j = 0;
                }
                break;

            case 0:
                break;

            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 0);

    free(fila);
    return 0;
}