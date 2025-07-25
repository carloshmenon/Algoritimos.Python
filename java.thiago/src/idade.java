

//IMPORTAR O SCANNER 

import java.util.Scanner;

public class idade {
    public static void main(String[] args) {
        //declarar o scanner dentro da main

        int num = 0 ;
        Scanner scan = new Scanner (System.in);
        System.out.println("digite sua idade : ");
        num=scan.nextInt();

        if(num >=18){
            System.out.println("Maior!!");
        }else{
            System.out.println("Menor!!");
        }

        System.out.println("sua idade é de  "+num);

        scan.close();

    }
}

