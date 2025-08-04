//Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas
//com os valores invertidos.

import java.util.Scanner;
public class exer9 {
    
    public static void main(String[] args) {
      
        int num1, num2;

        Scanner scan= new Scanner(System.in);
        System.out.println("digite um numero: ");
        num1= scan.nextInt();
        System.out.println("digite outro numero: ");
        num2= scan.nextInt();

        num2=(num2-num1);
        num1=(num1+num2);

        System.out.println("Invertendo os valores, "+ num1 +" agora é o primeiro número" + 
        " e " + num2+ " é o segundo número.");



    }
}
