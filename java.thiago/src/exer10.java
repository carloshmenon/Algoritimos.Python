///Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
///• O número digitado ao quadrado;
///• A raiz quadrada do número digitado;


import java.util.Scanner;
public class exer10 {
    
    public static void main(String[] args) {
        double num;

        Scanner scan= new Scanner(System.in);
        System.out.println("digite um numero : ");
        num= scan.nextDouble();
        
        if (num>=0){
            double num1= Math.sqrt(num);
            System.out.printf("a raiz quadrada %.2f e ", num1);
            System.out.println("o numero ao quadrado é "+ (num*num));

        }
        

    }
}
