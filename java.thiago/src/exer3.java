//Crie um programa que receba dois números e mostre qual deles é o maior

import java.util.Scanner;
public class exer3 {
    
    public static void main(String[] args) {
        
        int num1, num2;
        Scanner scan = new Scanner(System.in);
        System.out.println("digite um numero: ");
        num1=scan.nextInt();
        System.out.println("digite outro numero: ");
        num2=scan.nextInt();

        if (num1>num2) {
            System.out.printf("o numero um, %d é maior que o numero dois, %d. ",num1, num2);
            
        }else{
            System.out.printf("o numero dois, %d é maior que o numero um, %d. ",num2, num1);
        }


    }
}
