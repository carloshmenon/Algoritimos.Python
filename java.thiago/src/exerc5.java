//Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:
//F - Feminino, M – Masculino ou Sexo Inválido.


import java.util.Scanner;
public class exerc5 {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.println("digite seu sexo: M ou F");
        String sexo= scan.next();

        if (sexo.equalsIgnoreCase("M")){
            System.out.println("sexo masculino");

        }else if (sexo.equalsIgnoreCase("F")){
            System.out.println("sexo feminino");
            
        }else{
            System.out.println("digite M ou F!");
        }


    }
}
