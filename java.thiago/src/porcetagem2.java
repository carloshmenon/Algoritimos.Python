//usando o print de varias variaveis usando %
//no caso aqui a ordem das porcetagens esta dando print por ondem, comencando pelo nome 


public class porcetagem2
{
	public static void main(String[] args) {
	    
	    
	String nome= "carlos";
	String cidade= "campo grande";
	String apelido= "carlao";
	int idade=29;
	
	System.out.printf (" ola %s voce mora em %s e seu apelido é %s voce é muito legal e tem %d anos", nome, cidade,apelido,idade);
	
// a %s puxa o dado da string que tem uma variavel declarada
//já a %d puxa o dado de int, no caso a idade de 29
	  
	}
}
