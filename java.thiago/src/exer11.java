//Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar

import java.util.Scanner;
public class exer11 {
    public static void main(String[] args) {
        int num;
        Scanner scan = new Scanner(System.in);
        System.out.println("digite um numero: ");
        num=scan.nextInt();

        if(num%2==0);{
            System.out.println("o numero é par " + num);
        }else{
            System.out.println("o numero é impar");
        }

    
    }
}
