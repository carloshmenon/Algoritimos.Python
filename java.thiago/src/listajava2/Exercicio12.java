/*
12. Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais
de 0 até N em ordem crescente.
*/
import java.util.Scanner;

public class Exercicio12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo N: ");
        int N = sc.nextInt();

        for (int i = 0; i <= N; i++) {
            System.out.println(i);
        }
        sc.close();
    }
}
