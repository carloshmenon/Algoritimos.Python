// Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de
// acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de
// um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não
// concedido, caso contrário imprima: Empréstimo concedido.


import java.util.Scanner;
public class exer16 {
    public static void main(String[] args) {
        double salario, prestacao, emprestimo;

        Scanner scan= new Scanner(System.in);
        System.out.println("Digite seu salario ");
        salario=scan.nextInt();
        System.out.println("Digite o valor da prestação ");
        prestacao=scan.nextInt();

        emprestimo=salario*0.20;

        if(prestacao>emprestimo){
            System.out.println("Emprestimo liberado.");
        }else{
            System.out.println("emprestimo negado.");
        }
    }
    
}