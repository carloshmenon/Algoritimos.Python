
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 5

typedef struct {
    int senha;
    char nome[50];
} Paciente;

int main() {
    Paciente *fila = malloc(MAX * sizeof(Paciente));
    int qtd = 0, proximaSenha = 1, opcao;

    do {
        printf("\n1 - Chegada\n2 - Chamar proximo\n3 - Mostrar fila\n0 - Sair\nOpcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            if (qtd == MAX) {
                printf("Fila cheia! Paciente nao cadastrado.\n");
            } else {
                printf("Nome: ");
                scanf(" %49[^\n]", fila[qtd].nome);
                fila[qtd].senha = proximaSenha++;
                printf("Senha: %d\n", fila[qtd].senha);
                qtd++;
            }
        }
        else if (opcao == 2) {
            if (qtd == 0) {
                printf("Fila vazia!\n");
            } else {
                printf("Chamando: senha %d - %s\n", fila[0].senha, fila[0].nome);
                for (int i = 0; i < qtd - 1; i++)
                    fila[i] = fila[i + 1];
                qtd--;
            }
        }
        else if (opcao == 3) {
            if (qtd == 0) {
                printf("Fila vazia!\n");
            } else {
                for (int i = 0; i < qtd; i++)
                    printf("Senha %d - %s\n", fila[i].senha, fila[i].nome);
            }
        }
    } while (opcao != 0);

    free(fila);
    return 0;
}