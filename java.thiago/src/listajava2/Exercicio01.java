

/*
1. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após contagem.
*/
public class Exercicio01 {
    public static void main(String[] args) {
        int i = 10;
        while (i >= 0) {
            System.out.println(i);
            i--;
        }
        System.out.println("FIM!");
    }
}
