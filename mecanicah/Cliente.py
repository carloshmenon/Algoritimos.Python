from Database import Database


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
        dados=self.db.select()
        return dados
    
    def buscar_por_id(self, id):
        self.db = Database()
        clientes=self.db.select_by_id(id)
        return clientes
    
    def deletar(self,id):
        self.db=Database()
        deletee=self.db.delete(id)
        return deletee
        
cli= Cliente()

##excluindo 
# id_excluir= input("digite o nome do cliente que gostaria de deletar: ")
# retorno= cli.deletar(id_excluir)

# if retorno== True:
#     print("cliente excluido com sucessoooo")

# #cadastrando

# cli=Cliente()
# cli.nome= input("Digite seu nome: ")
# cli.cpf=input("Digite seu cpf: ")
# cli.fone=input("Digite seu fone: ")
# cli.cidade=input("Digite seu cidade: ")

# cli.cadastrar()

# clientes=cli.buscar()
# print(clientes)

clientes = cli.buscar()

for item in clientes:
    print(item)

id_atualizar= int(input("qual id deseja atualizar? "))
cli_att= cli.buscar_por_id(id_atualizar)
print(cli_att) 

cli_att=list(cli_att)
cli_att[1]=input("digite o novo nome: ")
cli_att[2]=input("digite o novo cpf: ")
cli_att[3]=input("digite o novo fone: ")
cli_att[4]=input("digite o novo cidade: ")

print(cli_att)
