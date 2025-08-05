// Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários
// acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor
// do seu salário líquido.


import java.util.Scanner;
public class exer15 {
    public static void main(String[] args) {
        double horas,salariobruto, salarioliquido ;
        Scanner scan = new Scanner(System.in);
        System.out.println("digite quantas horas trabalhadas");
        horas=scan.nextInt();

        salariobruto=((horas*40.5));

        if (salariobruto>2500){
            salarioliquido=salariobruto-(salariobruto*0.11);
            System.out.println("Seu salario liquido desse mes foi "+ salarioliquido);
        }else{
            System.out.println("seu salario liquido foi : "+ salariobruto);
        }
    }
}
