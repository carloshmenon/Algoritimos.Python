import java.util.Scanner;

public class Carro {
    private int portas; // atributo de um carro qualquer
    private String placa; // atributo de um carro qualquer 

    public String gertplaca(){//get pega a informação e retorna ela 
        return placa;
    }

    public int getportas(){// pega a informação de quantas portas temos
        return portas;
    }

    public void setplaca(String placa){// set modifica a placa, atribui valor ao objeto 
        this.placa=placa;
    }

    public void setportas(int portas){// set modifica a placa, atribui valor ao objeto 
        this.portas = portas;
    }

    public static void main(String[] args) {
       Scanner input = new Scanner (System.in);

       Carro car1 = new Carro();// aqui o scanner é o objeto carro e a variavel o car1, nao precisa pegar o Scanner como no comentario acima 
       //car1.portas =4; posso declarar a variavel fixa dele

       Carro car2 =new Carro();
       car2.placa = "nova placa";
       car2.portas= 5;
       System.out.println("Digite a quantidade de portas: ");// input para deixar a placa variada
       car1.portas = input.nextInt();
       System.out.println("Digite a placa do carro: ");
       //car1.placa = "HSX-4444"; posso declarar a placa fixa do car1
       car1.placa=input.next();
       System.out.println(car1.placa);

       car1.setplaca("H20-1111");
       System.out.println(car1.placa);
       
       car1.setportas(5);
       System.out.println(car1.portas);

       input.close();


    }
}
