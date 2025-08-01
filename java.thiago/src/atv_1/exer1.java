// 1. Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro
// com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
// digitado ao cubo

import java.util.Scanner;

package atv_1;


public class exer1 ;
public static void main(String[] args) {
        
     

    Scanner entrada = new Scanner(System.in);

    int n=5 ; //tamanho do vetor 
    int vet [] =new int [n]; // declaração do vetor "v"
    int i; // indice ou posição 

    // entrada de dados 
    for (i= 0; i< n; i++){
        System.out.printf("Informe %2d° o valor de %d ", (i+1),n);
        vet[i]= entrada.nextInt();

    }
    entrada.close();
}
