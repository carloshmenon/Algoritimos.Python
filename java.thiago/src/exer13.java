//Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números
//forem iguais, imprima a mensagem: Números iguais.

import java.util.Scanner;

public class exer13{
    public static void main(String[] args) {
      
        int num1, num2;
        Scanner scan= new Scanner(System.in);
        System.out.println("Digite um numero: ");
        num1=scan.nextInt();
        System.out.println("Digite outro numero: ");
        num2=scan.nextInt();
        scan.close();

        if (num1>num2){
            System.out.println("o primeiro numero é maior que o segundo.");
        }if (num2>num1){  
            System.out.println("o segundo numero é maior que o primeiro.");
        }else if(num1==num2){
            System.out.println("os numeros são iguais.");
        }

    }
  

    
        
}
