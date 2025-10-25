
    /*
2. Crie um programa que determine e mostre os 5 primeiros números ímpares, considerando
números maiores que 0.
*/
public class Exercicio02 {
    public static void main(String[] args) {
        int count = 0, num = 1;
        while (count < 5) {
            if (num % 2 != 0) {
                System.out.println(num);
                count++;
            }
            num++;
        }
    }
}


