public class Exercicio03 {
    /*
3. Crie um programa que determine e mostre os 10 primeiros números pares, considerando
números maiores que 0.
*/

    public static void main(String[] args) {
        int count = 0, num = 1;
        while (count < 10) {
            if (num % 2 == 0) {
                System.out.println(num);
                count++;
            }
            num++;
        }
    }


    
}
