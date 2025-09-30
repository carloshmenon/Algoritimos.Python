###herança###


class Funcionario:
    def __init__ (self,nome,login,senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    def logar(self):
        print (f" {self.nome} logado com sucesso ")

    def alterar_senha (self, nova_senha):
        self.senha = nova_senha
        return True
    
class Gerente(Funcionario):#a classe gerente esta herdando a classe funcionarios
    def __init__(self,nome,login,senha,setor): #aqui colocamos os requisitos do gerente
        super().__init__(nome, login, senha)#qui ele herda os requistos do funcionario
        self.setor= setor
        
    def logar(self): #polimorfismo
        confirm= input ("digite o token: " )
        if confirm:
            print(f" Gerente {self.nome} logado com sucesso no setor: {self.setor}")
        

luan=Gerente("luan victor", "lulu@gmail.com","1234","vendas") #aqui estamos definindo o usuario que sera o gerente
luan.logar()
luan.alterar_senha("78945")
print(luan.senha)






f1= Funcionario("eliandro","lili@gmail.com","1234")
f2= Funcionario("carlos","boaboa@gmail.com","12345")
