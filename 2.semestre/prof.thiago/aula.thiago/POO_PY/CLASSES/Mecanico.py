

class Mecanico: #letra inicial sempre maiuscula
    def __init__(self,nome,matricula,nivel): #construtor
        self.nome=nome
        self.matricula = matricula
        self.nivel=nivel
        self.salario=0

    def passar_orcamento(self):
        print("seu carro ficou tanto..." )

    def realizar_diagnostico(self):
        print(f"{self.nome} diagnosticando o veiculo ... ")

    def get_salario(self):
        return self.salario
    
    def set_salario (self, valor):
        self.salario= valor

    def calcular_comissao(self,servicos):
        comissao= servicos *0.15
        self.salario += comissao
        return True

mec1= Mecanico("carlos","1234","N1") #em ordem nome, matricula e nivel

mec1.passar_orcamento #aqui eu chamo a def do "passar orcamento" que ira dar print no texto 
mec1.realizar_diagnostico # aqui ele da o print igual

sal=mec1.get_salario()#aqui definimos uma nova variavel "sal" de salario e como ele começa zerado ele printa "0"
print(sal)

mec1.set_salario(5000) #aqui chamamos o comando .set e colocamos um valor dentro dos paranteses         
sal =mec1.get_salario() #aqui definimos uma nova variavel "sal2" para pegar o .set da linha acima e armazenar a informação

print(sal)

sal =mec1.get_salario()
print(sal)
mec1.calcular_comissao(9000)
print (f"salario atual {mec1.nome} R$ {mec1.get_salario()}")
