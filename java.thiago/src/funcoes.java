

public class funcoes {
    public static void main(String[] args) {
        hello();
        hello2("carlos");
        hello3("carlos",33);
        soma(10, 20);
        int res = soma(50,50); //aqui colocamos os valores
        System.out.println(res);//aqui guardamos o resultado
        String name= myname();//como ela esta vazia eu preciso de um conteudo 
        System.out.println(name);//aqu eu armazeno o conteudo no caso a str "carlos"
        double imcpeao=imc(100, 1.79);
        double imcpeao2 =imc2(150,1.80);
        String status2= "obesidade \n";
        System.out.printf(status2);

        String status =  "Gordao demais";

        System.out.printf("seu imc é de %f %s",imcpeao,status);


    }
    //funcao do tipo void nao retorna nada!!!
    public static void hello () {
        System.out.println("Helooooooo!!");
    }
    //aqui colocamos um paramentro dentro da funcao hello2
    public static void hello2 (String nome ) {
        System.out.printf("hello %s!!", nome);
        
    }//aqui colocamos dois paramettros dentro da classe hello3 um str e um int
    public static void hello3(String nome, int idade) {
        System.out.printf("\n heloooo %s voce tem %d !!\n", nome, idade);
        
    }

    public static int soma (int x, int y){ //aqui definimos a funcao
        int sum = x+y; //aqui definimos a operação
        return sum; //aqui pegamos o valor guardado em "res" e damos o print 
    }

    public static String myname(){
        return "carlos"; //aqui colocamos a o conteudo do parametro no return
    }

    public static double imc(double peso, double altura){//aqui calculamos valores com virgulas
        double myimc = peso/ (altura*altura);
        return myimc;
    }

    public static double imc2(double peso, double altura){//aqui retornamos uma string ao inves do resultado
        double myimc2 =peso/ (altura*altura);
        return myimc2;
    }

}
