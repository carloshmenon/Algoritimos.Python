// Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro
// com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
// digitado ao cubo


public class exerc1 { 
    public static void main(String[] args) {
        int x,y;
        float z;
        x=10;
        y=20;
        z=1.5f;

        System.out.println("primeiro produto mais a metade do segundo "+ ((x)+ (y/2)));
        System.out.println("o tripro do primeiro mais o terceiro "+((x*3)+(z)));
        System.out.println("o terceito numero ao cubo "+Math.pow (z,3));

       
        



    }
}
