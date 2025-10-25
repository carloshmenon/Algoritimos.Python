
/*
10. Crie um programa que leia um número inteiro N e depois imprima os N primeiros números
naturais ímpares.
*/
import java.util.Scanner;

public class Exercicio10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número inteiro N: ");
        int N = sc.nextInt();
        int count = 0, num = 1;

        while (count < N) {
            if (num % 2 != 0) {
                System.out.println(num);
                count++;
            }
            num++;
        }
        sc.close();
    }
}
