from Datebase import Database


class Cliente:
    def __init__ (self,nome=None, cpf= None, fone=None, cidade=None):
        self.nome=nome
        self.cpf=cpf
        self.fone=fone
        self.cidade=cidade
        

    def cadastrar(self):
        self.db= Database()
        tupla = (self.nome, self.cpf,self.fone, self.cidade)
        result= self.db.insert(tupla)
        return result
    
    def buscar(self):
        self.db = Database()
        dados=self.db.select
        return dados
    
    def deletar(self,id):
        self.db=Database()
        deletee=self.db.delete(id)
        return deletee
        
deletee= Cliente()


id= input("digite o nome do cliente que gostaria de deletar: ")

delet= deletee.deletar(id)

# cli=Cliente()
# cli.nome= input("Digite seu nome: ")
# cli.cpf=input("Digite seu cpf: ")
# cli.fone=input("Digite seu fone: ")
# cli.cidade=input("Digite seu cidade: ")

# cli.cadastrar()

# clientes=cli.buscar()
# print(clientes)


        
