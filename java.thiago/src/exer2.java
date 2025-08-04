// Crie um programa que receba um número inteiro e verifique se ele é maior que 10 se sim,
// imprima: é maior que 10, senão imprima: é menor que 10

import java.util.Scanner;

public class exer2 {
    
    public static void main(String[] args) {

        int num;
        Scanner scan = new Scanner (System.in);
        System.out.println("digite um numero : ");
        num=scan.nextInt();
        scan.close();

        if (num >10){
            System.out.println("esse numero é maior ou igual a 10, "+ num);
        }else{
            System.out.println("esse numero é menor que 10.");
        }

        

    }
}
