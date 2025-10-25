import java.util.Scanner;

public class exercicio08 {
       public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int soma = 0, count = 0;
        while (count < 10) {
            System.out.print("Digite um número positivo: ");
            int num = sc.nextInt();
            if (num > 0) {
                soma += num;
                count++;
            } else {
                System.out.println("Número ignorado (não positivo).");
            }
        }
        double media = soma / 10.0;
        System.out.println("Média: " + media);
        sc.close();
    }
}
