#include <stdio.h>

int main() {
    int n, i, j;
    int trocas = 0;

  
    printf("Digite a quantidade de produtos: ");
    scanf("%d", &n);

    float precos[n];

    
    printf("Digite os precos dos produtos:\n");
    for (i = 0; i < n; i++) {
        printf("Preco %d: ", i + 1);
        scanf("%f", &precos[i]);
    }

   
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (precos[j] > precos[j + 1]) {
               
                float temp = precos[j];
                precos[j] = precos[j + 1];
                precos[j + 1] = temp;
                
                trocas++;
            }
        }
    }

   
    printf("\n--- Precos Ordenados ---\n");
    for (i = 0; i < n; i++) {
        printf("R$ %.2f\n", precos[i]);
    }

    printf("\nTotal de trocas realizadas: %d\n", trocas);

    return 0;
}