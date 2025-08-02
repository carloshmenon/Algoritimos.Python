//Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim
//como a diferença existente entre ambos.


import java.util.Scanner;
public class exer12 {
    public static void main(String[] args) {    
        int num1, num2,num3, num4 ;
        Scanner scan = new Scanner(System.in);
        System.out.println("digite um numero: ");
        num1=scan.nextInt();
        System.out.println("digite outro numero: ");
        num2=scan.nextInt();
        num3=(num1-num2);
        num4=(num2-num1);


        if (num1>num2){
            System.out.printf(
                "o numero um %d é o maior, a diferença entre o %d e o %d é de %d ", num1, num1, num2,num3);
        }if (num2>num1){
            System.out.printf(
                "o numero um %d é o maior, a diferença entre o %d e o %d é de %d ", num2, num2, num1,num4);

        }

        
    }
}
