clientes=[]
class Pessoa:
    def __init__(self,nome):
        self.nome=nome

class Conta:
    def __init__(self,agência, conta,sacar,senha, saldo=0):
        
        self.agência=agência
        self.conta=conta
        self.senha=senha
        self.saldo=saldo 
        self.sacar=sacar
        self.extrato=[]


    def adicionar_cliente(self, clientes:object):
        self.clientes.append(clientes)

    def preencher_dados(self):
        self.nome= input("digite seu nome: ")
        self.conta= int(input("numero da conta: "))
        self.agência= int(input("Agência: "))
        self.senha=int(input("Senha: "))
        print("cadastrada com sucesso")

    def depositar(self, valor):
        if valor>0:
            self.saldo+= valor
            self.extrato.append
            print(f"Depósito de {valor} realizado com sucesso! ")

        else:
            print("valor inválido para depósito")
            



       