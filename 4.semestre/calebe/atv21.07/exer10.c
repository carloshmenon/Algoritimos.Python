#include <stdio.h>

int main() {

    int tipo;
    float valor, total;

    printf("Digite o valor do produto: ");
    scanf("%f", &valor);

    printf("Digite o tipo do produto: ");
    scanf("%d", &tipo);

    if (tipo == 0)
    {
        total = valor + (valor * 0.10);
    }

    if (tipo != 0)
    {
        total = valor + (valor * 0.20);
    }

    printf("Valor final: %.2f", total);

    return 0;
}