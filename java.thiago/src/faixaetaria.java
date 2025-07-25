
import java.util.Scanner;

public class faixaetaria {
    public static void main(String[] args) {
        

        Scanner input= new Scanner(System.in);
        int idade;
        System.out.println("Digite sua idade ");
        idade =input.nextInt();
        input.close();

        if(idade<=12){
            System.out.println("Criança!!");
        }
        else if(idade> 12 && idade<= 17){
            System.out.println("Adolescente");
        }
        else if (idade>17 && idade <+59){
            System.out.println("Adulto");
        }
        else {
            System.out.println("Idoso!!");

        }

        input.close();
    }
}
