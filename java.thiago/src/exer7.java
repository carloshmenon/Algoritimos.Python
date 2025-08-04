// Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor
// de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser
// vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, crie um
// algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

import java.util.Scanner;
public class exer7 {
    public static void main(String[] args) {
        
        int num;

        Scanner scan = new Scanner(System.in);
        System.out.println("qual valor da aquisição? ");
        num=scan.nextInt();

        if (num<=50){
            System.out.println("o produto com 45% de lucro deverá ser vendido por, " + (num*1.45));
        }else {
            System.out.println("o produto com 30% de lucro deverá ser vendido por, " + (num*1.30));
        }
    }
}
