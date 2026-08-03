#include <stdio.h>

int main() {

    int opcao;
    float saldo = 1000.00;
    float valor;

    while (opcao != 0) {

        printf("\n========================\n");
        printf("   CAIXA ELETRONICO\n");
        printf("========================\n");
        printf("1 - Consultar saldo\n");
        printf("2 - Depositar\n");
        printf("3 - Sacar\n");
        printf("0 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch(opcao) {

            case 1:
                printf("Saldo: R$ %.2f\n", saldo);
                break;

            case 2:
                printf("Digite o valor do deposito: ");
                scanf("%f", &valor);

                saldo = saldo + valor;

                printf("Deposito realizado!\n");
                break;

            case 3:
                printf("Digite o valor do saque: ");
                scanf("%f", &valor);

                if (valor <= saldo) {
                    saldo = saldo - valor;
                    printf("Saque realizado!\n");
                } else {
                    printf("Saldo insuficiente!\n");
                }

                break;

            case 0:
                printf("Obrigado por utilizar o caixa!\n");
                break;

            default:
                printf("Opcao invalida!\n");
        }

    }

    return 0;
}
