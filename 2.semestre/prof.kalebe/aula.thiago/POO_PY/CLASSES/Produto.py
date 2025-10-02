

class Produto:
    def __init__(self,nome,marca,modelo,preco):
        self.nome = nome
        self.marca= marca
        self.modelo=modelo
        self.preco=preco
        self.__inicia_prod()

    def get_nome(self): #metodo get
        return self.nome
    
    def __inicia_prod(self): ##metodo privado
        print ("produto inicializado com sucesso!")

## caso vejamos esse codigo abaixo eu vou ter ctz que essa classe esta sendo executada do proprio arquivo

if __name__ == "__main__":
    prod1=Produto ("Notebook", "Dell", "Core I9",9500)
    print("executando do proprio arquivo...")
#-----------------------------------------------------------------------


prod1 = Produto("Notebook", "Dell", "Core I9",9500)
nome_prod = prod1.get_nome()
print(nome_prod)
