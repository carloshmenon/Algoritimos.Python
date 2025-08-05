// Crie um programa que leia 2 notas de um aluno, verifique
//  se as notas são válidas e exiba na tela a média destas 
// notas. Uma nota válida deve ser, obrigatoriamente, um valor
//  entre 0.0 e 10.0. Caso a nota não seja válida, esse
//   fato deve ser informado ao usuário e o programa termina.


import java.util.Scanner;
public class exerc14 {
    public static void main(String[] args) {
        int num1, num2;
        Scanner scan=new Scanner(System.in);
        System.out.println("Digite a primeira nota: ");
        num1=scan.nextInt();
        System.out.println("digite a segunda note: ");
        num2=scan.nextInt();

        if (num1>0){
            System.out.println("A media do aluno é "+ (num1/num2));

        }else if(num1<0){
            System.out.println("digite uma nota valida! ");
        }
    }
}
