#include <stdio.h>

int main() {
    int n, i, j;
    int codigoProcurado;

    
    printf("Digite a quantidade de clientes cadastrados: ");
    scanf("%d", &n);

    int vetorOriginal[n];
    int vetorOrdenado[n];

    printf("Digite os codigos dos clientes:\n");
    for (i = 0; i < n; i++) {
        printf("Codigo %d: ", i + 1);
        scanf("%d", &vetorOriginal[i]);
        
        vetorOrdenado[i] = vetorOriginal[i];
    }

    printf("\nDigite o codigo do cliente que deseja buscar: ");
    scanf("%d", &codigoProcurado);

   
    int compSequencial = 0;
    int encontradoSequencial = -1;

    for (i = 0; i < n; i++) {
        compSequencial++;
        if (vetorOriginal[i] == codigoProcurado) {
            encontradoSequencial = i;
            break;
        }
    }

    
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (vetorOrdenado[j] > vetorOrdenado[j + 1]) {
                int temp = vetorOrdenado[j];
                vetorOrdenado[j] = vetorOrdenado[j + 1];
                vetorOrdenado[j + 1] = temp;
            }
        }
    }

    
    int compBinaria = 0;
    int inicio = 0, fim = n - 1;
    int encontradoBinaria = -1;

    while (inicio <= fim) {
        int meio = inicio + (fim - inicio) / 2;
        compBinaria++;

        if (vetorOrdenado[meio] == codigoProcurado) {
            encontradoBinaria = meio;
            break;
        } else if (vetorOrdenado[meio] < codigoProcurado) {
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }

   
    printf("\n--- RESULTADOS DA BUSCA ---\n");
    
    if (encontradoSequencial != -1) {
        printf("Busca Sequencial: Codigo encontrado na posicao %d.\n", encontradoSequencial);
    } else {
        printf("Busca Sequencial: Codigo nao encontrado.\n");
    }
    printf("Comparacoes feitas na Busca Sequencial: %d\n", compSequencial);

    printf("\n");

    if (encontradoBinaria != -1) {
        printf("Busca Binaria: Codigo encontrado no vetor ordenado.\n");
    } else {
        printf("Busca Binaria: Codigo nao encontrado.\n");
    }
    printf("Comparacoes feitas na Busca Binaria: %d\n", compBinaria);

    return 0;
}