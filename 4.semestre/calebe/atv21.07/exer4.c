#include <stdio.h>

int main() {

    int num1, num2;

    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    printf("O primeiro numero e maior? %d\n", num1 > num2);
    printf("O segundo numero e maior? %d\n", num2 > num1);

    return 0;
}