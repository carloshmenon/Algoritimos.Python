package exer.matriz;

public class exer1 {
    public static void main(String[] args) {
        
        int matriz[][]= new int [3][3];

        //1 linha

        matriz[0][0]=1;
        matriz[0][1]=2;
        matriz[0][2]=3;

        //2 LINHA
        matriz[1][0]=4;
        matriz[1][1]=5;
        matriz[1][2]=6;

        //3 LINHA
        matriz[2][0]=7;
        matriz[2][1]=8;
        matriz[2][2]=9;

        int i,j; //i= linha j =colunas

        for (i=0; i<matriz.length; i++){
            System.out.printf("", (i+1));
            for (j=0; j<matriz[i].length;j++){
                System.out.printf("%d", matriz[i][j]);

            }
        }   System.out.println("\n");
        
        

        
    }
}
