#include <stdio.h>

int main() {

    int numero;

    printf("Digite um numero: ");
    scanf("%d", &numero);

    if (numero > 0)
    {
        printf("Numero positivo");
    }

    if (numero < 0)
    {
        printf("Numero negativo");
    }

    if (numero == 0)
    {
        printf("Numero igual a zero");
    }

    return 0;
}