# Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:
# Nome
# Idade
# Endereço
# A classe deve ter os seguintes métodos:
# Mostrar nome;
# Alterar a idade;
# Imprimir endereço.

class Pessoa:
    def __init__ (self, nome, idade, endereco):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
    
    def hello(self):
        print(f"ola {self.nome}")

    def idad(self):
        print(f"sua idade: {self.idade}")

    def end(self):
        print(f"seu endereço: {self.endereco}")

p1=Pessoa("carlos", "18","rua tal")

p1.hello()
p1.idade=19
print(p1.idade)
p1.end()