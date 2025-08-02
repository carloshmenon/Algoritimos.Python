// Crie um Programa que pergunte em que turno você estuda.
//  Peça para digitar M - Matutino ou VVespertino ou N - Noturno. 
//  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
// "Valor Inválido!", conforme o caso
import java.util.Scanner;
public class exer6 {
    
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.println("digite seu turno: M- matutino, V- vespertino, ou N-noturno.");
        String sexo= scan.next();

        if (sexo.equalsIgnoreCase("M")){
            System.out.println("BOM DIA!!");

        }else if (sexo.equalsIgnoreCase("V")){
            System.out.println("BOA TARDE!!");
            
        }
        else if (sexo.equalsIgnoreCase("N")){
            System.out.println("BOA NOITE!!");}
        else{
            System.out.println("digite uma opcao valida");
        }

    }
}
