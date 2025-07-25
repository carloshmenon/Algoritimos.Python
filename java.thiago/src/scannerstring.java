import java.util.Scanner;

public class scannerstring {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite SIM ou NÃO");
        String confirmacao= scan.next();
        scan.close();
        System.out.println("TEXTO DIGITADO FOI "+confirmacao);
        scan.close();
    }
}
