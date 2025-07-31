package aula_30_07;

import java.util.Scanner;

public class vetor4 {

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
    
}
 