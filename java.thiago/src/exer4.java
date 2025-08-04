//Crie um programa que receba três números e mostre-os se estão em ordem crescente.


import java.util.Scanner;
public class exer4 {
    public static void main(String[] args) {
        int num1, num2, num3;
    
        Scanner scan = new Scanner(System.in);
        System.out.println("digite um numero: ");
        num1=scan.nextInt();
        System.out.println("digite outro numero: ");
        num2=scan.nextInt();
        System.out.println("digite outro numero: ");
        num3=scan.nextInt();

        if (num1>=num2 && num1>num3){
            System.out.printf("a ordem crescente é essa: %d, %d, %d" , num1, num2,num3);
        }if (num2>=num1 && num2>num3) {
            System.out.printf("a ordem crescente é essa: %d, %d, %d" , num2, num1,num3);
            
        }else{
            System.out.printf("a ordem crescente é essa: %d, %d, %d" , num3, num2,num1);
        }

        
    }    
}
