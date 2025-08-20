package matriz;

//criando matriz 

//int m[][]= new int [3][3]; aqui criamos uma matriz com 3 linhas e 3 colunas 
public class matriz2 {
    public static void main(String[] args) {

        int m[][]= new int[3][3];
        
        //1° linha 
        m[0][0]=1;  
        m[0][1]=2;  
        m[0][2]=3;
        
        //2°LINHA 
        m[1][0]= 4;
        m[1][1]= 5;
        m[1][2]= 6;

        //3° LINHA
        m[2][0]= 7;
        m[2][1]= 8;
        m[2][2]= 9;

        System.out.println(m[2][0]);

        int i,j; //I=LINHAS J= COLUNAS

        for (i=0; i<m.length; i++){//ESSE lenght percorre as linhas e conta elas 
            System.out.printf("%d linha: ", (i+1));//print coloca as linhas da matriz
            for (j=0; j<m[i].length;j++){//esse lenght contas quantos itens temos dentro de cada i, no caso da linha 0 ele conta quantos itens temos na linha 0
                System.out.printf("%d", m[i][j]);// aqui printamos os itens contados
                
            }
            System.out.println("\n");
        }
    }

    
}
