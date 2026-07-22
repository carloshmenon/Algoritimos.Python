#include <stdio.h>

int main() {

    float distancia, tempo, velocidade;

    printf("Digite a distancia: ");
    scanf("%f", &distancia);

    printf("Digite o tempo: ");
    scanf("%f", &tempo);

    velocidade = distancia / tempo;

    printf("Velocidade: %.2f", velocidade);

    return 0;
}