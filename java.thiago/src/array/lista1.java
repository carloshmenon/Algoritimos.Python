package array;

import java.util.ArrayList;
import java.util.List;


public class lista1 {
    public static void main(String[] args) {

        List<String> listanomes = new ArrayList<>();
        listanomes.add("alan");
        listanomes.add("luan");
        listanomes.add("carlos");
        listanomes.add("jow");
        listanomes.add("perterson");
        listanomes.add(1, "gerson");
        
        
        System.out.println(listanomes.size());  //imprime o tamanho da lista
        listanomes.remove(2);//removi o item 2 da lista
        System.out.println(listanomes.size()); //  imprime o tamanho da lista sem o item 2 
        System.out.println(listanomes.get(3)); // get imprime o conteudo que esta na lista na posição 3 "jow"

        String nome = listanomes.get(2);
        System.out.println(nome);   
        listanomes.set(4, "jose do egito" );// set é para trocar o nome, aqui trocamos o gerson por jose do egito
        String novo_nome= listanomes.get(4);// aqui atribuimos a variavel novo_nome a listanomes na posição 4 , assim fazendo a substituição
        System.out.println(novo_nome);// aqui fazemos o print somente da variavel 
        
    }
}
