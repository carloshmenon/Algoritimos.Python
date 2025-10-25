/*
11. Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50
primeiros números pares.
*/
public class Exercicio11 {
    public static void main(String[] args) {
        int soma = 0;
        int count = 0;
        int num = 0;

        while (count < 50) {
            soma += num;
            num += 2;
            count++;
        }

        System.out.println("Soma dos 50 primeiros pares: " + soma);
    }
}
