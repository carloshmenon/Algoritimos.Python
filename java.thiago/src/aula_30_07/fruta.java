package aula_30_07;
public class fruta {
    
    public static void main(String[] args) {
        
        //lista de compras no hortiftui
        String[] frutas= {"banana","Maça", "kiwi","Mamão"};
        // entre chaves{}os elementos Strings do vetor 
        String fruta_preferida =frutas[1];
        System.out.println("minha fruta preferida é: "+fruta_preferida);

        for (int i=0; i<frutas.length; i++) {
            System.out.println(frutas[i]);
        }
    }
}
