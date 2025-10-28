
class Cliente:
    def __init__(self,id,nome,cpf,email,tel):
        self.id=id
        self.nome=nome
        self.cpf=cpf
        self.email=email
        self.tel=tel

    def cadastro (self):
        print(f"cliente: {self.nome} | id {self.id} \n cadastrado com sucesso!! ")

    def atualizar(self, nome, email, tel):
        self.email = email
        self.tel=tel

class Produto:

    def __init__ (self, codigo, nome, desc, preco, qtd):
        self.codigo=codigo
        self.nome= nome
        self.desc=desc
        self.preco=preco
        self.qtd=qtd

    def atualizar(self, nova_qtd):
        self.qtd=nova_qtd
        print(f" estoque atualizado. Nova quantidade : {self.qtd}")

    def aplicar_desconto(self,percentual):
        preco_desc= self.preco - (self.preco*(percentual/100))
        return preco_desc
    
    def infos(self):
        print(f"nome do produto {self.nome} | preço {self.preco:.2f} | quantidade : {self.qtd}  ")

lista_clientes=[]
cliente1= Cliente(1, "alan", "000000000","alan.faltante", "099999999999999")
lista_clientes.append(cliente1)
print (lista_clientes)

lista_produto=[]
prod1= Produto(1, "cera de brilho", 0, 100.00, 10 )
lista_produto.append(prod1)
print (lista_produto)
