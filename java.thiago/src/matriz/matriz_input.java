package matriz;

import java.util.Scanner;

public class matriz_input {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o numero de linhas: ");
        int linhas = scan.nextInt();
        System.out.println("Digite o numero de colunas: ");
        int colunas = scan.nextInt();

        int matriz[][] =new int[linhas][colunas];
        
    System.out.println("digite os elementos da matriz:");
    for (int i= 0; i<linhas; i++) {
        for (int j=0; j<colunas; j++){
            System.out.println("elemento [" + i + "][" + j + "]: ");
            matriz[i][j]= scan.nextInt();
        }
    }
    //exibindo a matriz

    System.out.println("\nMatriz preenchida");
    for (int i=0; i< linhas; i++){
        for(int j=0; j<colunas; j++){
            System.out.println(matriz[i][j]+ "");
        }
        System.out.println("");
    }
    scan.close();

    }
}
