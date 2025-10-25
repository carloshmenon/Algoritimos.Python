
import java.util.Scanner;

/*
9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
*/

public class Exercicio09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int menor = Integer.MAX_VALUE;
        int maior = Integer.MIN_VALUE;

        for (int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i + "º número: ");
            int num = sc.nextInt();
            if (num < menor) menor = num;
            if (num > maior) maior = num;
        }

        System.out.println("Menor valor: " + menor);
        System.out.println("Maior valor: " + maior);
        sc.close();
    }
}
