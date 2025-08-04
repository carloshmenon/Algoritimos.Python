//Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
//número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import java.util.Scanner;

public class exer8 {
    public static void main(String[] args) {
        double raizQuadrada ;

        Scanner scan= new Scanner (System.in);
        System.out.println("digite um numero");
        raizQuadrada=scan.nextDouble();

        if (raizQuadrada>=0){
            double num= Math.sqrt(raizQuadrada);
            System.out.printf("A raiz quadrada %.2f é ", num);
        }else{
            System.out.println("numero invalido!");
        }
    }
}
